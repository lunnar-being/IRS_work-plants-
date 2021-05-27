import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
        path:'/home',
        name:'home',
        component:()=> import("@/views/home")
    },
    {
        path:'/content',
        name:'content',
        component:()=> import('@/views/content')
    },
    {
        path:'/content2',
        name:'content2',
        component:()=> import('@/views/content2')
    }
]

const router = new VueRouter({
    routes
})

export default router