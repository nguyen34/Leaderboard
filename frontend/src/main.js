import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Axios from 'axios'



const app = createApp(App)

app.use(router)
app.config.globalProperties.$axios = Axios
app.config.globalProperties.$axios.defaults.withCredentials = true
app.config.globalProperties.$axios.defaults.baseURL = 'http://localhost:8000'
app.use(store)

app.mount('#app')
