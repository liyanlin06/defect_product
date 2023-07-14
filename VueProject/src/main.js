import { createApp } from 'vue'


import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

import App from './App.vue'
import router from "./router";
import {zhCn} from "element-plus/es/locale/index";
import './assets/global.css'
//axios.defaults.baseURL = '/api' //配置环境
import axios from 'axios'

createApp(App).use(router).use(ElementPlus,{locale:zhCn,}).mount('#app')
