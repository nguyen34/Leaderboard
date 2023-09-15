// First we need to import axios.js
import axios from "axios";
// Next we make an 'instance' of it

const LOCAL_URL = "http://localhost:8000/";
const baseURL = LOCAL_URL;
const instance = axios.create({
  // .. where we make our configurations
  baseURL: baseURL,
});
// Axios CSRF token setup
instance.defaults.xsrfCookieName = "csrftoken";
instance.defaults.xsrfHeaderName = "X-CSRFTOKEN";
instance.defaults.withCredentials = true;
// Also add/ configure interceptors && all the other cool stuff

export default instance;