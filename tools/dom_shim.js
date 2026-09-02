// minimal DOM shim for headless execution
var __nodes = {};
function mkNode(id) {
  return {
    id: id, style: {}, dataset: {}, hidden: false, value: "1", textContent: "",
    className: "", clientWidth: 400, offsetWidth: 100,
    attrs: {}, children: [],
    // innerHTML serialises the appended children (tag, attributes, text) so a headless
    // sweep can scan the rendered output for NaN / Infinity / undefined
    get innerHTML() { return this.children.map(function (c) { return "<" + (c.tag || "node") + " " +
      Object.keys(c.attrs).map(function (k) { return k + "=\"" + c.attrs[k] + "\""; }).join(" ") + ">" + c.textContent + c.innerHTML + "</" + (c.tag || "node") + ">"; }).join(""); },
    set innerHTML(v) { this.children = []; this._raw = v; },
    setAttribute: function (k, v) { this.attrs[k] = v; },
    getAttribute: function (k) { return this.attrs[k]; },
    appendChild: function (c) { this.children.push(c); c.parent = this; return c; },
    addEventListener: function () {},
    removeEventListener: function () {},
    remove: function () { if (this.parent) this.parent.children = this.parent.children.filter(function (x) { return x !== this; }, this); },
    querySelector: function () { return null; },
    querySelectorAll: function () { return []; },
    getBoundingClientRect: function () { return { left: 0, top: 0, width: 400, height: 300 }; },
    getContext: function () { return {
      createImageData: function (w, h) { return { data: new Uint8ClampedArray(w*h*4), width: w, height: h }; },
      putImageData: function () {},
    }; },
  };
}
var document = {
  body: mkNode("body"),
  documentElement: mkNode("html"),
  getElementById: function (id) { if (!__nodes[id]) __nodes[id] = mkNode(id); return __nodes[id]; },
  createElementNS: function (ns, name) { var n = mkNode("ns:" + name); n.tag = name; return n; },
  createElement: function (name) { var n = mkNode("el:" + name); n.tag = name; return n; },
};
var window = this;
function getComputedStyle() { return { getPropertyValue: function () { return "#123456"; } }; }
var localStorage = { getItem: function () { return null; }, setItem: function () {} };
var __rafCount = 0;
function requestAnimationFrame(fn) { __rafCount++; }
var performance = { now: function () { return Date.now(); } };
function addEventListener() {}
