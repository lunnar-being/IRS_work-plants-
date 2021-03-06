import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

// const routes = [
//     {
//         path:'/home',
//         name:'home',
//         component:()=> import("@/views/home")
//     },
//     {
//         path:'/content',
//         name:'content',
//         component:()=> import('@/views/content')
//     },
//     {
//         path:'/content2',
//         name:'content2',
//         component:()=> import('@/views/content2')
//     },
//     {
//         path:'/detail',
//         name:'detail',
//         component:()=> import('@/views/detail')
//     },
//     {
//         path:'/index',
//         name:'index',
//         component:()=> import('@/views/index')
//     }
// ]
const routes = [{
    path: '/login',
    name: 'login',
    component: () => import('@/views/login/index')
},
{
    path: '/register',
    name: 'register',
    component: () => import('@/views/register/index')
},
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
},
{
    path:'/detail',
    name:'detail',
    component:()=> import('@/views/detail')
},

{
    path:'/index',
    name:'index',
    component:()=> import('@/views/index')
},
{
    path:'/findPwd',
    name:'findPwd',
    component:()=>import('@/views/findPwd/index')
},
{
    path:'',
    redirect:'/store/index'
},
{
    path: '/store',
    component: () => import('@/views/layout/Layout'),
    children: [
    {
        path: 'category',
        name: 'category',
        component: () => import('@/views/category')
    },
    {
        path:'advanced',
        name:'advanced',
        component:()=>import('@/views/advanced')
    },
    {
        path:'result',
        name:'result',
        component:()=>import('@/views/result')
    },
    {
        path:'pictures',
        name:'pictures',
        component:()=>import('@/views/pictures')
    },
    {
        path:'contact',
        name:'contact',
        component:()=>import('@/views/contact')
    },
    {
        path:'index',
        name:'index',
        component:()=>import('@/views/index')
    },
    {
        path:'cart',
        name:'cart',
        component:()=>import('@/views/cart')
    }
    ,
    {
        path:'map',
        name:'map',
        component:()=>import('@/views/map')
    },
    {
        path:'center',
        name:'center',
        component:()=>import('@/views/center')
    },
    {
        path:'order',
        name:'order',
        component:()=>import('@/views/order')
    },
    {
        path:'a-steps',
        name:'a-steps',
        component:()=>import('@/views/a-steps')
    },
    {
        path:'upload',
        name:'upload',
        component:()=>import('@/views/upload')
    },
    {
        path:'features',
        name:'features',
        component:()=>import('@/views/features')
    },
    ]
}
]
const router = new VueRouter({
    routes
})

export default router