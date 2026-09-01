import math, random
random.seed(3)
H=8; XM=3.9; NV=1.5; LR=0.002
W1x=[(random.random()*2-1)*4/XM for _ in range(H)]
b1=[(random.random()*2-1)*2 for _ in range(H)]
W2=[(random.random()*2-1)/math.sqrt(H) for _ in range(H*H)]
b2=[0.0]*H
W3=[(random.random()*2-1)*0.3/math.sqrt(H) for _ in range(H)]
b3=[0.0]

def fwd(x):
    a1=[0]*H; d1=[0]*H; e1=[0]*H; z11=[0]*H
    for j in range(H):
        z=W1x[j]*x+b1[j]; z1=W1x[j]
        a=math.tanh(z); s=1-a*a
        a1[j]=a; z11[j]=z1; d1[j]=s*z1; e1[j]=-2*a*s*z1*z1
    a2=[0]*H; d2=[0]*H; e2=[0]*H; z21=[0]*H; z22=[0]*H
    for k in range(H):
        z=b2[k]; z1=0; z2=0
        for j in range(H):
            w=W2[k*H+j]; z+=w*a1[j]; z1+=w*d1[j]; z2+=w*e1[j]
        a=math.tanh(z); s=1-a*a
        a2[k]=a; z21[k]=z1; z22[k]=z2; d2[k]=s*z1; e2[k]=s*z2-2*a*s*z1*z1
    N=b3[0]; N1=0; N2=0
    for k in range(H):
        N+=W3[k]*a2[k]; N1+=W3[k]*d2[k]; N2+=W3[k]*e2[k]
    return N,N1,N2,(a1,d1,e1,z11,a2,d2,e2,z21,z22)

def residual(x):
    N,N1,N2,_=fwd(x)
    y=1+x*x*N; g=min(max(y,0),1.2)
    return 6*N+6*x*N1+x*x*N2+g**NV

def loss(pts):
    return sum(residual(x)**2 for x in pts)/len(pts)

def grads(pts):
    gW1x=[0.0]*H; gb1=[0.0]*H; gW2=[0.0]*(H*H); gb2=[0.0]*H; gW3=[0.0]*H; gb3=[0.0]
    M=len(pts)
    for x in pts:
        N,N1,N2,(a1,d1,e1,z11,a2,d2,e2,z21,z22)=fwd(x)
        y=1+x*x*N; g=min(max(y,0),1.2)
        r=6*N+6*x*N1+x*x*N2+g**NV
        dTerm=NV*g**(NV-1)*x*x if (0<y<1.2) else 0
        gr=2*r/M
        gN=gr*(6+dTerm); gN1=gr*6*x; gN2=gr*x*x
        ga=[0.0]*H; ga1=[0.0]*H; ga2=[0.0]*H
        for k in range(H):
            gW3[k]+=gN*a2[k]+gN1*d2[k]+gN2*e2[k]
            ga[k]=W3[k]*gN; ga1[k]=W3[k]*gN1; ga2[k]=W3[k]*gN2
        gb3[0]+=gN
        gz_=[0.0]*H; gz1_=[0.0]*H; gz2_=[0.0]*H
        for k in range(H):
            a=a2[k]; s=1-a*a; z1=z21[k]; z2=z22[k]
            gz = ga[k]*s + ga1[k]*(-2*a*s*z1) + ga2[k]*(s*(6*a*a-2)*z1*z1 - 2*a*s*z2)
            gz1= ga1[k]*s + ga2[k]*(-4*a*s*z1)
            gz2= ga2[k]*s
            gz_[k]=gz; gz1_[k]=gz1; gz2_[k]=gz2
            gb2[k]+=gz
            for j in range(H):
                gW2[k*H+j]+=gz*a1[j]+gz1*d1[j]+gz2*e1[j]
        ha=[0.0]*H; ha1=[0.0]*H; ha2=[0.0]*H
        for k in range(H):
            for j in range(H):
                w=W2[k*H+j]; ha[j]+=w*gz_[k]; ha1[j]+=w*gz1_[k]; ha2[j]+=w*gz2_[k]
        for j in range(H):
            a=a1[j]; s=1-a*a; z1=z11[j]
            gz = ha[j]*s + ha1[j]*(-2*a*s*z1) + ha2[j]*(s*(6*a*a-2)*z1*z1)
            gz1= ha1[j]*s + ha2[j]*(-4*a*s*z1)
            gW1x[j]+=gz*x+gz1
            gb1[j]+=gz
    return gW1x,gb1,gW2,gb2,gW3,gb3

pts=[0.02+(XM-0.02)*i/15 for i in range(16)]
# --- finite difference check ---
gA=grads(pts)
eps=1e-6; worst=0
params=[(W1x,gA[0],'W1x'),(b1,gA[1],'b1'),(W2,gA[2],'W2'),(b2,gA[3],'b2'),(W3,gA[4],'W3'),(b3,gA[5],'b3')]
for arr,g,name in params:
    for i in range(len(arr)):
        old=arr[i]
        arr[i]=old+eps; lp=loss(pts)
        arr[i]=old-eps; lm=loss(pts)
        arr[i]=old
        fd=(lp-lm)/(2*eps)
        err=abs(fd-g[i])/(abs(fd)+abs(g[i])+1e-10)
        if err>worst: worst=err; worstn=(name,i,fd,g[i])
print("worst relative gradient error:", worst, worstn)

# --- short training run with Adam ---
m={id(a):[0.0]*len(a) for a,_,_ in params}; v={id(a):[0.0]*len(a) for a,_,_ in params}
t=0
for step in range(4000):
    G=grads(pts); t+=1
    b1c=1-0.9**t; b2c=1-0.999**t
    for (arr,_,_),g in zip(params,G):
        M_=m[id(arr)]; V_=v[id(arr)]
        for i in range(len(arr)):
            M_[i]=0.9*M_[i]+0.1*g[i]
            V_[i]=0.999*V_[i]+0.001*g[i]*g[i]
            arr[i]-=LR*(M_[i]/b1c)/(math.sqrt(V_[i]/b2c)+1e-8)
    if step%1000==999: print("step",step+1,"loss",loss(pts))

# --- compare with RK4 ---
def rk4(n,xmax,npts=50):
    NS=4000; h=xmax/NS; x=1e-6; u=1-x*x/6; vv=-x/3; out=[(x,u)]
    f=lambda x,u,v:(v, -2*v/max(x,1e-9)-max(u,0)**n)
    for k in range(1,NS+1):
        A=f(x,u,vv); B=f(x+h/2,u+A[0]*h/2,vv+A[1]*h/2)
        Cc=f(x+h/2,u+B[0]*h/2,vv+B[1]*h/2); D=f(x+h,u+Cc[0]*h,vv+Cc[1]*h)
        u+=h/6*(A[0]+2*B[0]+2*Cc[0]+D[0]); vv+=h/6*(A[1]+2*B[1]+2*Cc[1]+D[1]); x+=h
        if k%(NS//npts)==0: out.append((x,u))
    return out
mx=0
for x,ye in rk4(NV,XM):
    N,_,_,_=fwd(x); yp=1+x*x*N
    mx=max(mx,abs(yp-ye))
print("max |PINN - RK4| after 4000 steps (H=8 tiny net):", mx)
