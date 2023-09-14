import { createStore } from 'vuex';
import test from '@/store/modules/test';



const store = createStore({
    modules: {
        test
    }
});

export default store