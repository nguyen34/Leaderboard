import './assets/main.css'
import "@mdi/font/css/materialdesignicons.css";
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Axios from 'axios'
import vuetify from '@/plugins/vuetify'

const app = createApp(App)

app.use(router)
app.config.globalProperties.$axios = Axios
app.config.globalProperties.$axios.defaults.withCredentials = true
app.config.globalProperties.$axios.defaults.baseURL = 'http://localhost:8000'
app.use(store)
app.use(vuetify)

app.mount('#app')
