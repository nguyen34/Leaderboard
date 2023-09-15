import { createStore } from 'vuex';
import userLeaderboards from '@/store/modules/userLeaderboards';



const store = createStore({
    modules: {
        userLeaderboards,
    }
});

export default store