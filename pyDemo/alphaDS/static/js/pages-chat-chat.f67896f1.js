(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["pages-chat-chat"],{1697:function(t,e,n){"use strict";n.r(e);var r=n("173e"),a=n.n(r);for(var o in r)["default"].indexOf(o)<0&&function(t){n.d(e,t,(function(){return r[t]}))}(o);e["default"]=a.a},"173e":function(t,e,n){"use strict";n("7a82");var r=n("4ea4").default;Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0;var a=r(n("5530")),o=r(n("2909")),i=r(n("c7eb")),u=r(n("1da1"));n("d3b7"),n("14d9"),n("498a"),n("99af"),n("ac1f");var c={data:function(){return{text:"",defaultList:[{state:1,text:"您好，我是小福，有任何问题，都可以问我哟~"},{state:1,text:"小福无所不能，我可以：\n\n\t\t\t\t1.撰写作文、论文、小说、剧本等，润色和修改已有文案；\n\n\t\t\t\t2.翻译中英文文档和文字;\n\n\t\t\t\t3.我可以作为您的倾诉对象和聆听者,为您解忧和讲故事；\n\n\t\t\t\t4.我可以扮演面试官、书籍人物等各种角色,模拟真实场景让您练习;\n\n\t\t\t\t5.除上述功能外,我还可以根据您的具体需求提供定制化服务。\n\n\t\t\t\t您可以尽量详细地描述需求,我会根据描述提供最匹配和精确的解决方案，您可以这样问我：\n\n\t\t\t\t例1:写一篇《XXX》读后感，\n\n\t\t\t\t例2:写一篇五一出游的英语作文，关于我和爸妈去桂林游玩\n\n\t\t\t\t例3:写一个能火的短视频剧本\n\n\t\t\t\t例4:给我讲一下泰坦尼克号这部电影\n\n\t\t\t\t例5:js电话号码正则表达式\n\n\t\t\t\t例6:你现在是面试官，开始和我对话.."}],historyObj:{state:"",text:""},talkList:[]}},mounted:function(){var t=[];[].forEach((function(e){if(e.state){var n={state:2,text:e.state};t.push(n)}if(e.text){var r={state:1,text:e.text};t.push(r)}})),0===t.length&&(t=this.defaultList),this.talkList=t,this.scrollBottom()},methods:{getList:function(){return(0,u.default)((0,i.default)().mark((function t(){var e;return(0,i.default)().wrap((function(t){while(1)switch(t.prev=t.next){case 0:return e={open_id:app.globalData.userInfo.openid},t.next=3,api.aichat(e);case 3:t.sent;case 4:case"end":return t.stop()}}),t)})))()},sendInfo:function(){var t=this;return(0,u.default)((0,i.default)().mark((function e(){var n,r,u;return(0,i.default)().wrap((function(e){while(1)switch(e.prev=e.next){case 0:if(t.text&&t.text.trim()){e.next=3;break}return uni.showToast({title:"请输入文字",icon:"error",duration:2e3}),e.abrupt("return");case 3:return n=t.talkList,r={state:2,text:t.text},n.push(r),t.talkList=n,t.historyObj={state:t.text,text:""},t.scrollBottom(),e.next=11,t.repeatInfo();case 11:u=[],u=[].concat((0,o.default)(u),[(0,a.default)({},t.historyObj)]),t.text="",t.historyObj={state:"",text:""};case 15:case"end":return e.stop()}}),e)})))()},repeatInfo:function(){var t=this;return(0,u.default)((0,i.default)().mark((function e(){var n,r,a,o,u,c;return(0,i.default)().wrap((function(e){while(1)switch(e.prev=e.next){case 0:if(t.text){e.next=3;break}return uni.showToast({title:"未获取到文本",icon:"error",duration:2e3}),e.abrupt("return");case 3:return uni.showLoading({title:"正在组织语言",mask:!0}),n={vx_msg:t.text},e.next=7,api.aichat(n);case 7:r=e.sent,200===r.code&&(a=r.data.hf,o={state:1,text:a||"不好意思，您的问题无法回答"},u=t.talkList,c=t.historyObj,c.text=a,u.push(o),t.historyObj=c,t.talkList=u,uni.hideLoading(),t.scrollBottom());case 9:case"end":return e.stop()}}),e)})))()},scrollBottom:function(){uni.createSelectorQuery().select("#chat-box").boundingClientRect((function(t){uni.pageScrollTo({scrollTop:t.height+30,duration:300})})).exec()}}};e.default=c},"1da1":function(t,e,n){"use strict";function r(t,e,n,r,a,o,i){try{var u=t[o](i),c=u.value}catch(s){return void n(s)}u.done?e(c):Promise.resolve(c).then(r,a)}n("7a82"),Object.defineProperty(e,"__esModule",{value:!0}),e.default=function(t){return function(){var e=this,n=arguments;return new Promise((function(a,o){var i=t.apply(e,n);function u(t){r(i,a,o,u,c,"next",t)}function c(t){r(i,a,o,u,c,"throw",t)}u(void 0)}))}},n("d3b7")},"1dda":function(t,e,n){var r=n("24fb");e=r(!1),e.push([t.i,"#chat-box[data-v-0bf1bf9a]{padding-bottom:75px}.img_box[data-v-0bf1bf9a]{height:50px;width:50px;overflow:hidden;\n  /*超出边框隐藏*/border-radius:50px;text-align:center;\n  /*子元素居中 */background-color:#fff;margin:5px}.head_portrait[data-v-0bf1bf9a]{height:80%;padding:10% 0 0}.dialog[data-v-0bf1bf9a]{white-space:pre-line;background-color:#fff;border-radius:0 10px 10px 10px;padding:5px 5px 5px 5px;max-width:calc(100% - 50px - 60px);\n  /*输入框最大宽度，根据文字调整*/margin:30px 0 0 5px;box-shadow:0 0 5px #999;\n  /*下 右 阴影长度 阴影颜色*/box-sizing:border-box\n  /*输入框最大宽度减去padding宽度*/}.dialog_box[data-v-0bf1bf9a]{display:flex}.student_box[data-v-0bf1bf9a]{flex-direction:row-reverse\n  /*对话框父级元素从左往右*/}.student_dialog[data-v-0bf1bf9a]{border-radius:10px 0 10px 10px}.i_put[data-v-0bf1bf9a]{height:40px;background-color:#fff;border-radius:15px 15px 15px 15px;box-shadow:0 0 5px #999;flex:1;\n  /*父级元素剩余空间填充满*/margin-left:10px}.input_box[data-v-0bf1bf9a]{position:fixed;bottom:20px;width:100%;z-index:999;\n  /*position属性优先级设置，高不会被挡住*/display:flex\n  /*按钮和输入框在同一行*/}.input_box .i_send[data-v-0bf1bf9a]{border-radius:30px;height:40px;width:40px;overflow:hidden;background-color:#fff;margin:0 10px 0 10px;display:flex;\n  /*为了使align-items和justify-content两个生效*/align-items:center;\n  /*上下对齐*/justify-content:center;\n  /*左右对齐*/padding:0 5px;box-shadow:0 0 5px #999}.image_send[data-v-0bf1bf9a]{width:25px}.input_box uni-input[data-v-0bf1bf9a]{padding-left:15px}",""]),t.exports=e},2909:function(t,e,n){"use strict";n("7a82"),Object.defineProperty(e,"__esModule",{value:!0}),e.default=function(t){return(0,r.default)(t)||(0,a.default)(t)||(0,o.default)(t)||(0,i.default)()};var r=u(n("6005")),a=u(n("db90")),o=u(n("06c5")),i=u(n("3427"));function u(t){return t&&t.__esModule?t:{default:t}}},3427:function(t,e,n){"use strict";n("7a82"),Object.defineProperty(e,"__esModule",{value:!0}),e.default=function(){throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")},n("d9e2"),n("d401")},6005:function(t,e,n){"use strict";n("7a82"),Object.defineProperty(e,"__esModule",{value:!0}),e.default=function(t){if(Array.isArray(t))return(0,r.default)(t)};var r=function(t){return t&&t.__esModule?t:{default:t}}(n("6b75"))},"61bb":function(t,e,n){"use strict";n.d(e,"b",(function(){return r})),n.d(e,"c",(function(){return a})),n.d(e,"a",(function(){}));var r=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("v-uni-view",{attrs:{id:"chat-box"}},[t._l(t.talkList,(function(e){return n("v-uni-view",{staticClass:"dialog_box",class:2===e.state?"student_box":""},[n("v-uni-view",{staticClass:"img_box"},[1===e.state?n("v-uni-image",{staticClass:"head_portrait",attrs:{src:"/static/image/user.jpg",mode:"heightFix"}}):n("v-uni-image",{staticClass:"head_portrait",attrs:{src:"/static/image/student.png",mode:"heightFix"}})],1),n("v-uni-view",{staticClass:"dialog",class:2===e.state?"student_dialog":""},[t._v(t._s(e.text))])],1)})),n("v-uni-view",{staticClass:"input_box"},[n("v-uni-input",{staticClass:"i_put",attrs:{type:"text",placeholder:"请输入你的问题",bindinput:"getInputInfo",maxlength:"200"},model:{value:t.text,callback:function(e){t.text=e},expression:"text"}}),n("v-uni-button",{staticClass:"i_send",attrs:{size:"mini"},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.sendInfo.apply(void 0,arguments)}}},[n("v-uni-image",{staticClass:"image_send",attrs:{src:"/static/image/send.png",mode:"widthFix"}})],1)],1)],2)},a=[]},"9c16":function(t,e,n){"use strict";var r=n("f9ee"),a=n.n(r);a.a},a70e:function(t,e,n){"use strict";n.r(e);var r=n("61bb"),a=n("1697");for(var o in a)["default"].indexOf(o)<0&&function(t){n.d(e,t,(function(){return a[t]}))}(o);n("9c16");var i=n("f0c5"),u=Object(i["a"])(a["default"],r["b"],r["c"],!1,null,"0bf1bf9a",null,!1,r["a"],void 0);e["default"]=u.exports},b636:function(t,e,n){var r=n("e065");r("asyncIterator")},c7eb:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default=function(){
/*! regenerator-runtime -- Copyright (c) 2014-present, Facebook, Inc. -- license (MIT): https://github.com/facebook/regenerator/blob/main/LICENSE */
e.default=function(){return t};var t={},n=Object.prototype,a=n.hasOwnProperty,o=Object.defineProperty||function(t,e,n){t[e]=n.value},i="function"==typeof Symbol?Symbol:{},u=i.iterator||"@@iterator",c=i.asyncIterator||"@@asyncIterator",s=i.toStringTag||"@@toStringTag";function f(t,e,n){return Object.defineProperty(t,e,{value:n,enumerable:!0,configurable:!0,writable:!0}),t[e]}try{f({},"")}catch(M){f=function(t,e,n){return t[e]=n}}function l(t,e,n,r){var a=e&&e.prototype instanceof p?e:p,i=Object.create(a.prototype),u=new E(r||[]);return o(i,"_invoke",{value:L(t,n,u)}),i}function d(t,e,n){try{return{type:"normal",arg:t.call(e,n)}}catch(M){return{type:"throw",arg:M}}}t.wrap=l;var h={};function p(){}function v(){}function b(){}var x={};f(x,u,(function(){return this}));var g=Object.getPrototypeOf,y=g&&g(g(P([])));y&&y!==n&&a.call(y,u)&&(x=y);var m=b.prototype=p.prototype=Object.create(x);function w(t){["next","throw","return"].forEach((function(e){f(t,e,(function(t){return this._invoke(e,t)}))}))}function _(t,e){var n;o(this,"_invoke",{value:function(o,i){function u(){return new e((function(n,u){(function n(o,i,u,c){var s=d(t[o],t,i);if("throw"!==s.type){var f=s.arg,l=f.value;return l&&"object"==(0,r.default)(l)&&a.call(l,"__await")?e.resolve(l.__await).then((function(t){n("next",t,u,c)}),(function(t){n("throw",t,u,c)})):e.resolve(l).then((function(t){f.value=t,u(f)}),(function(t){return n("throw",t,u,c)}))}c(s.arg)})(o,i,n,u)}))}return n=n?n.then(u,u):u()}})}function L(t,e,n){var r="suspendedStart";return function(a,o){if("executing"===r)throw new Error("Generator is already running");if("completed"===r){if("throw"===a)throw o;return I()}for(n.method=a,n.arg=o;;){var i=n.delegate;if(i){var u=j(i,n);if(u){if(u===h)continue;return u}}if("next"===n.method)n.sent=n._sent=n.arg;else if("throw"===n.method){if("suspendedStart"===r)throw r="completed",n.arg;n.dispatchException(n.arg)}else"return"===n.method&&n.abrupt("return",n.arg);r="executing";var c=d(t,e,n);if("normal"===c.type){if(r=n.done?"completed":"suspendedYield",c.arg===h)continue;return{value:c.arg,done:n.done}}"throw"===c.type&&(r="completed",n.method="throw",n.arg=c.arg)}}}function j(t,e){var n=e.method,r=t.iterator[n];if(void 0===r)return e.delegate=null,"throw"===n&&t.iterator["return"]&&(e.method="return",e.arg=void 0,j(t,e),"throw"===e.method)||"return"!==n&&(e.method="throw",e.arg=new TypeError("The iterator does not provide a '"+n+"' method")),h;var a=d(r,t.iterator,e.arg);if("throw"===a.type)return e.method="throw",e.arg=a.arg,e.delegate=null,h;var o=a.arg;return o?o.done?(e[t.resultName]=o.value,e.next=t.nextLoc,"return"!==e.method&&(e.method="next",e.arg=void 0),e.delegate=null,h):o:(e.method="throw",e.arg=new TypeError("iterator result is not an object"),e.delegate=null,h)}function O(t){var e={tryLoc:t[0]};1 in t&&(e.catchLoc=t[1]),2 in t&&(e.finallyLoc=t[2],e.afterLoc=t[3]),this.tryEntries.push(e)}function k(t){var e=t.completion||{};e.type="normal",delete e.arg,t.completion=e}function E(t){this.tryEntries=[{tryLoc:"root"}],t.forEach(O,this),this.reset(!0)}function P(t){if(t){var e=t[u];if(e)return e.call(t);if("function"==typeof t.next)return t;if(!isNaN(t.length)){var n=-1,r=function e(){for(;++n<t.length;)if(a.call(t,n))return e.value=t[n],e.done=!1,e;return e.value=void 0,e.done=!0,e};return r.next=r}}return{next:I}}function I(){return{value:void 0,done:!0}}return v.prototype=b,o(m,"constructor",{value:b,configurable:!0}),o(b,"constructor",{value:v,configurable:!0}),v.displayName=f(b,s,"GeneratorFunction"),t.isGeneratorFunction=function(t){var e="function"==typeof t&&t.constructor;return!!e&&(e===v||"GeneratorFunction"===(e.displayName||e.name))},t.mark=function(t){return Object.setPrototypeOf?Object.setPrototypeOf(t,b):(t.__proto__=b,f(t,s,"GeneratorFunction")),t.prototype=Object.create(m),t},t.awrap=function(t){return{__await:t}},w(_.prototype),f(_.prototype,c,(function(){return this})),t.AsyncIterator=_,t.async=function(e,n,r,a,o){void 0===o&&(o=Promise);var i=new _(l(e,n,r,a),o);return t.isGeneratorFunction(n)?i:i.next().then((function(t){return t.done?t.value:i.next()}))},w(m),f(m,s,"Generator"),f(m,u,(function(){return this})),f(m,"toString",(function(){return"[object Generator]"})),t.keys=function(t){var e=Object(t),n=[];for(var r in e)n.push(r);return n.reverse(),function t(){for(;n.length;){var r=n.pop();if(r in e)return t.value=r,t.done=!1,t}return t.done=!0,t}},t.values=P,E.prototype={constructor:E,reset:function(t){if(this.prev=0,this.next=0,this.sent=this._sent=void 0,this.done=!1,this.delegate=null,this.method="next",this.arg=void 0,this.tryEntries.forEach(k),!t)for(var e in this)"t"===e.charAt(0)&&a.call(this,e)&&!isNaN(+e.slice(1))&&(this[e]=void 0)},stop:function(){this.done=!0;var t=this.tryEntries[0].completion;if("throw"===t.type)throw t.arg;return this.rval},dispatchException:function(t){if(this.done)throw t;var e=this;function n(n,r){return i.type="throw",i.arg=t,e.next=n,r&&(e.method="next",e.arg=void 0),!!r}for(var r=this.tryEntries.length-1;r>=0;--r){var o=this.tryEntries[r],i=o.completion;if("root"===o.tryLoc)return n("end");if(o.tryLoc<=this.prev){var u=a.call(o,"catchLoc"),c=a.call(o,"finallyLoc");if(u&&c){if(this.prev<o.catchLoc)return n(o.catchLoc,!0);if(this.prev<o.finallyLoc)return n(o.finallyLoc)}else if(u){if(this.prev<o.catchLoc)return n(o.catchLoc,!0)}else{if(!c)throw new Error("try statement without catch or finally");if(this.prev<o.finallyLoc)return n(o.finallyLoc)}}}},abrupt:function(t,e){for(var n=this.tryEntries.length-1;n>=0;--n){var r=this.tryEntries[n];if(r.tryLoc<=this.prev&&a.call(r,"finallyLoc")&&this.prev<r.finallyLoc){var o=r;break}}o&&("break"===t||"continue"===t)&&o.tryLoc<=e&&e<=o.finallyLoc&&(o=null);var i=o?o.completion:{};return i.type=t,i.arg=e,o?(this.method="next",this.next=o.finallyLoc,h):this.complete(i)},complete:function(t,e){if("throw"===t.type)throw t.arg;return"break"===t.type||"continue"===t.type?this.next=t.arg:"return"===t.type?(this.rval=this.arg=t.arg,this.method="return",this.next="end"):"normal"===t.type&&e&&(this.next=e),h},finish:function(t){for(var e=this.tryEntries.length-1;e>=0;--e){var n=this.tryEntries[e];if(n.finallyLoc===t)return this.complete(n.completion,n.afterLoc),k(n),h}},catch:function(t){for(var e=this.tryEntries.length-1;e>=0;--e){var n=this.tryEntries[e];if(n.tryLoc===t){var r=n.completion;if("throw"===r.type){var a=r.arg;k(n)}return a}}throw new Error("illegal catch attempt")},delegateYield:function(t,e,n){return this.delegate={iterator:P(t),resultName:e,nextLoc:n},"next"===this.method&&(this.arg=void 0),h}},t},n("7a82"),n("a4d3"),n("e01a"),n("d3b7"),n("d28b"),n("3ca3"),n("ddb0"),n("b636"),n("944a"),n("0c47"),n("23dc"),n("3410"),n("d9e2"),n("d401"),n("14d9"),n("159b"),n("131a"),n("26e9"),n("fb6a");var r=function(t){return t&&t.__esModule?t:{default:t}}(n("53ca"))},db90:function(t,e,n){"use strict";n("7a82"),Object.defineProperty(e,"__esModule",{value:!0}),e.default=function(t){if("undefined"!==typeof Symbol&&null!=t[Symbol.iterator]||null!=t["@@iterator"])return Array.from(t)},n("a4d3"),n("e01a"),n("d3b7"),n("d28b"),n("3ca3"),n("ddb0"),n("a630")},f9ee:function(t,e,n){var r=n("1dda");r.__esModule&&(r=r.default),"string"===typeof r&&(r=[[t.i,r,""]]),r.locals&&(t.exports=r.locals);var a=n("4f06").default;a("6d8e6f80",r,!0,{sourceMap:!1,shadowMode:!1})}}]);