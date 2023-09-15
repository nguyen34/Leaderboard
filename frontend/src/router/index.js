import { createRouter, createWebHistory } from 'vue-router'
import LeaderBoardView from '../views/LeaderBoardView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'LeaderBoard',
      component: LeaderBoardView
    },
  ]
})

export default router
