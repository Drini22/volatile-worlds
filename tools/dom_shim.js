// minimal DOM shim for headless execution
var __nodes = {};
function mkNode(id) {
  return {
    id: id, style: {}, dataset: {}, hidden: false, value: "1", innerHTML: "", textContent: "",
    className: "", clientWidth: 400, offsetWidth: 100,
    attrs: {},
    setAttribute: function (k, v) { this.attrs[k] = v; },
    getAttribute: function (k) { return this.attrs[k]; },
    appendChild: function (c) { return c; },
    addEventListener: function () {},
    removeEventListener: function () {},
    remove: function () {},
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
  createElementNS: function (ns, name) { return mkNode("ns:" + name); },
  createElement: function (name) { return mkNode("el:" + name); },
};
var window = this;
function getComputedStyle() { return { getPropertyValue: function () { return "#123456"; } }; }
var localStorage = { getItem: function () { return null; }, setItem: function () {} };
var __rafCount = 0;
function requestAnimationFrame(fn) { __rafCount++; }
var performance = { now: function () { return Date.now(); } };
function addEventListener() {}
