(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["pages-signIn-signIn"],{"014e":function(n,t,i){"use strict";var e=i("94cf"),a=i.n(e);a.a},"94cf":function(n,t,i){var e=i("d654");e.__esModule&&(e=e.default),"string"===typeof e&&(e=[[n.i,e,""]]),e.locals&&(n.exports=e.locals);var a=i("4f06").default;a("0043c9fb",e,!0,{sourceMap:!1,shadowMode:!1})},9809:function(n,t,i){"use strict";i.r(t);var e=i("ba32"),a=i("f1f6");for(var u in a)["default"].indexOf(u)<0&&function(n){i.d(t,n,(function(){return a[n]}))}(u);i("014e");var s=i("f0c5"),o=Object(s["a"])(a["default"],e["b"],e["c"],!1,null,"501b527f",null,!1,e["a"],void 0);t["default"]=o.exports},b5cc:function(n,t,i){"use strict";i("7a82"),Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var e=i("ba1b"),a={data:function(){return{phone:""}},methods:{signIn:function(){var n=(0,e.validatePhoneNumber)(this.phone);n||uni.showToast({title:"手机号格式不正确，请检查",icon:"none"})}}};t.default=a},ba1b:function(n,t,i){"use strict";i("7a82"),Object.defineProperty(t,"__esModule",{value:!0}),t.validatePhoneNumber=function(n){return/^(1[0-9][0-9])\d{8}$/.test(n)},i("ac1f"),i("00b4")},ba32:function(n,t,i){"use strict";i.d(t,"b",(function(){return e})),i.d(t,"c",(function(){return a})),i.d(t,"a",(function(){}));var e=function(){var n=this,t=n.$createElement,i=n._self._c||t;return i("v-uni-view",{staticClass:"signIn-page"},[i("v-uni-view",{staticClass:"signIn-box"},[i("v-uni-view",{staticClass:"sb-title"},[n._v("手机号注册")]),i("v-uni-view",{staticClass:"s-input"},[i("v-uni-input",{staticClass:"uni-input",attrs:{placeholder:"请输入手机号"},model:{value:n.phone,callback:function(t){n.phone=t},expression:"phone"}})],1),i("v-uni-view",{staticClass:"s-btn"},[i("v-uni-button",{attrs:{type:"primary"},on:{click:function(t){arguments[0]=t=n.$handleEvent(t),n.signIn.apply(void 0,arguments)}}},[n._v("注册")])],1)],1)],1)},a=[]},d654:function(n,t,i){var e=i("24fb");t=e(!1),t.push([n.i,".signIn-box[data-v-501b527f]{padding-top:100px}.sb-title[data-v-501b527f]{text-align:center;font-size:22px;font-weight:700}.s-input[data-v-501b527f]{margin:20px 0 20px 0;padding:0 25px}.s-input .uni-input[data-v-501b527f]{background-color:#fff;height:40px;padding:0 10px}.s-btn[data-v-501b527f]{width:85%;margin:30px auto 0}",""]),n.exports=t},f1f6:function(n,t,i){"use strict";i.r(t);var e=i("b5cc"),a=i.n(e);for(var u in e)["default"].indexOf(u)<0&&function(n){i.d(t,n,(function(){return e[n]}))}(u);t["default"]=a.a}}]);