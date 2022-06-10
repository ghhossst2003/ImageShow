import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import router from './router'
import 'lib-flexible'
import VueCookies from 'vue-cookies'

createApp(App).use(router).use(ElementPlus).use(VueCookies).mount('#app')
