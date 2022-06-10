import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'
import MainView from '../views/MainView.vue'

const routes = [
  {
    path: '/',
    name: 'main',
    component: MainView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/upload',
    name: 'upload',
    component: () => import('../views/UploadView.vue')
  },
  {
    path: '/test',
    name: 'test',
    component: () => import('../views/TestView.vue')
  },
  {
      path: '/login',
      name: 'login',
      component: ()=> import('../views/LoginView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
