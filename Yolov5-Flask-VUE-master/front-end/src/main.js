// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import InstantSearch from 'vue-instantsearch'
import axios from 'axios'
import Element from 'element-ui'
import './plugins/ant-design-vue.js'
import router from "./plugins/router"
import echarts from "echarts";

Vue.prototype.$echarts = echarts;
import '../node_modules/element-ui/lib/theme-chalk/index.css'
import '../src/assets/style.css'
import './theme/index.css'

Vue.use(Element)
Vue.use(InstantSearch)
Vue.config.productionTip = false
Vue.prototype.$http = axios

Vue.component("App", App);

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    render: h => h(App)
}).$mount('#app')
