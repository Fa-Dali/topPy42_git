// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCZ1oayix_MSoHOmjygI4JWUOOOQ1ItjiY",
  authDomain: "todos-1165d.firebaseapp.com",
  projectId: "todos-1165d",
  storageBucket: "todos-1165d.firebasestorage.app",
  messagingSenderId: "81583736231",
  appId: "1:81583736231:web:2564b3091ab1b2639ee282",
  databaseURL: "https://todos-1165d-default-rtdb.europe-west1.firebasedatabase.app/"
};

// Initialize Firebase
// const app = initializeApp(firebaseConfig);

const firebaseApp = initializeApp(firebaseConfig);
export default firebaseApp
