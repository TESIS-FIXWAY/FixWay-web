// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyD2qT1SvHYr7Y9Mfnbegb5jW28s3VqMiFU",
  authDomain: "dbtesis-2fe55.firebaseapp.com",
  projectId: "dbtesis-2fe55",
  storageBucket: "dbtesis-2fe55.appspot.com",
  messagingSenderId: "499310183533",
  appId: "1:499310183533:web:3a3b4de1e11be862832b64",
  measurementId: "G-T3XJ098RMG"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);