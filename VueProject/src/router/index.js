import { createRouter, createWebHistory } from 'vue-router'
import Layout from '../Layout/Layout.vue'

const routes = [



    {
        path: '/',
        redirect:'/single',
        name: 'Layout',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../Layout/Layout.vue'),
        children:[
            {
                path: '/single',
                name: 'single',
                // route level code-splitting
                // this generates a separate chunk (about.[hash].js) for this route
                // which is lazy-loaded when the route is visited.
                component: () => import(/* webpackChunkName: "about" */ '../views/single.vue')
            },
            {
                path: '/mul',
                name: 'mul',
                // route level code-splitting
                // this generates a separate chunk (about.[hash].js) for this route
                // which is lazy-loaded when the route is visited.
                component: () => import(/* webpackChunkName: "about" */ '../views/mul.vue')
            },

        ],

    },



]


const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes
})
export default router
