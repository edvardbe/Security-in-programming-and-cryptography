<script setup lang="ts">
import authService from '@/services/authService';
import { ref } from 'vue';

const username = ref('');
const password = ref('');
const message = ref('');
</script>

<template>
    <main>
    <div class="box">
        <h2>Login</h2>
        <input v-model="username" placeholder="username" />
        <input type="password" v-model="password" placeholder="password" />
        <button @click="authService.login(username, password)">Sign in</button>
        <div class="msg">{{ message }}</div>
        </div>
    </main>
</template>

<style>
.box{
  display: flex;
  flex-direction: column;
  max-width: 20vw;
}
</style>