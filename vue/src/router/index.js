import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DashboardView from '../views/DashboardView.vue'
import CreateSetView from '../views/CreateSetView.vue'
import ShowAllSetsView from '../views/ShowAllSetsView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: DashboardView
  },
  {
    path: '/create',
    name: 'create',
    component: CreateSetView
  },
  {
    path: '/show-all',
    name: 'show-all',
    component: ShowAllSetsView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
