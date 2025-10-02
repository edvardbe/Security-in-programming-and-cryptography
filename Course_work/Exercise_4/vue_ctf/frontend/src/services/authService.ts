import axios from 'axios'

const authClient = axios.create({
  baseURL: 'http://localhost:3000/api',
  headers: { 'Content-Type': 'application/json' },
  withCredentials: true,
})

const authService = {
    async login(email: string, password: string): Promise<void> {
        try {
        const response = await authClient.post('/login', {
            email: email,
            password: password,
            })

        if (response.status === 200) {
            sessionStorage.setItem('jwt', response.data.token);
        }
        } catch (error: any) {
        console.error('Error in login', error);
        }
    }
};


export default authService;