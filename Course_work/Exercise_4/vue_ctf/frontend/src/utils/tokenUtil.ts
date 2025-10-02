import { jwtDecode } from 'jwt-decode';
import { ref } from 'vue';

const token = ref<string | null>(sessionStorage.getItem('jwt'));

export function isTokenExpired(token: string) {
        try {
            const decodedToken = jwtDecode(token) as { exp: number };
            const currentTime = Math.floor(Date.now() / 1000);
            return decodedToken.exp < currentTime;
        } catch (error) {
            console.error('Error decoding token:', error);
            return true;
        }
    }

export const isTokenValid = () => {
  if (!token.value) {
    return false;
  }
  if (isTokenExpired(token.value)) {
    console.log('Token is expired');
    return false;
  } else {
    console.log('Token is valid');
    return true;
  }
}