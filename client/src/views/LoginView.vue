<template>
    <div>
        <main>
            <div class="login-box">
                <el-form :model="loginForm">
                    <el-form-item>
                        <el-input v-model="loginForm.username" 
                                  placeholder="please input username"> 
                        </el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-input v-model="loginForm.password"
                                    type="password" 
                                    auto-complete="off" 
                                    placeholder="please input password">
                        </el-input>
                    </el-form-item>
                </el-form>
                <p id="loginPrompt">{{loginPromptRef}}</p>
                <div>
                    <el-button type="primary" @click="submitLoginInfo(loginForm)">Login</el-button>
                </div>
                
            </div>
            
        </main>
    </div>
</template>


<script lang="ts" setup>
import config from "@/assets/config";
import axios from "axios";
import { onBeforeMount, reactive, ref,} from "vue";
import Cookies from 'js-cookie';
import router from "@/router";

const loginPromptRef = ref("")

type LoginForm = {
    username:string,
    password:string,
}

const loginForm = reactive<LoginForm>({
    username: "1111",
    password: "1111",
})

const isSuccessLogin = (uid:number, token:string)=>{
    console.log(uid)
    console.log(token)
    Cookies.set('uid', uid.toString())
    Cookies.set('token', token)
    router.push({path: '/upload'})
}

const submitLoginInfo = (data:LoginForm) => {
    // console.log(typeof(Proxy))
    // console.log(data.username)
    // console.log(data.password)
    const url = config.url.login 
    axios.get(url, {
        params: data
    }).then(response => {
        if(response.status === 200) {
            const responseMsg = eval(response.data)
            if(responseMsg.status === 0) {
                console.log(responseMsg.data)
                const loginData = JSON.parse(responseMsg.data)
                console.log("loginData:", loginData)
                console.log("typeof loginData:", typeof(loginData))
                isSuccessLogin(loginData['id'], loginData['token'])
            } else {
                loginPromptRef.value = responseMsg.message
                console.log(loginPromptRef.value!)
            }
        }else{
            loginPromptRef.value = 'server error!'
        }
    }).catch(error => {
        loginPromptRef.value = 'server error!'
        console.log(error)
    })
}

onBeforeMount(() => {
    const uid = Cookies.get("uid")
    const token = Cookies.get("token")
    console.log(uid)
    console.log(token)
    if((uid!=undefined)&&(token!=undefined)) {
        router.push({path: '/upload'})
    }
})
</script>

<style scoped>
#loginPrompt {
    color: red;
    text-align: center;
}
.login-box {
    background: rgb(246, 248, 250);
    width: 308px;
    padding: 16px;
    border: 1px solid;
    border-color: #d0d7de;
    margin: 0px auto;
}

.btn-box {
    width: 100%;
}

.el-button {
    width: 100%;
}
</style>
