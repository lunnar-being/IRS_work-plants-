// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import './plugins/axios'
import App from './App'
import InstantSearch from 'vue-instantsearch'
import axios from 'axios'
axios.defaults.headers.post['Content-Type']='application/json'
import Element from 'element-ui'
import './plugins/ant-design-vue.js'
import router from "./plugins/router"
import echarts from "echarts";
import VueAMap from "vue-amap";Vue.use(VueAMap)
// import { AMapManager } from "vue-amap";
import VueAwesomeSwiper from 'vue-awesome-swiper'

Vue.prototype.$echarts = echarts;
import '../node_modules/element-ui/lib/theme-chalk/index.css'
import '../src/assets/style.css'
import './theme/index.css'

Vue.use(Element)
Vue.use(InstantSearch)

Vue.use(VueAwesomeSwiper)


Vue.component("App", App);

VueAMap.initAMapApiLoader({
    key: "e532a122aa9183214d573d0541841e43",
    plugin: ["AMap.Autocomplete", "AMap.Geocoder",'AMap.Scale', "AMap.Geolocation","AMap.CircleEditor","AMap.PolyEditor","AMap.ToolBar","AMap.PlaceSearch",],
    v: "1.4.15",
    uiVersion: "1.1"
  });
/* eslint-disable no-new */
Vue.config.productionTip = false
Vue.prototype.$http = axios
new Vue({
    el: '#app',
    router,
    render: h => h(App)
}).$mount('#app')
