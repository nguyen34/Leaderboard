import axios from '@/plugins/axios';

export default {
    namespaced: true,
    state: {
        users: [],
    },
    mutations: {
        setUsers(state, users) {
            state.users = users;
        },

        addUser(state, user) {
            state.users.push(user);
        },

        deleteUser(state, user) {
            state.users.splice(state.users.indexOf(user), 1);
        },   

        incrementUserScore(state, user) {
            state.users[state.users.indexOf(user)].points++;
        },

        decrementUserScore(state, user) {
            if (state.users[state.users.indexOf(user)].points > 0)  {
                state.users[state.users.indexOf(user)].points--;
            }
        }

    },

    actions: {
        async fetchUsers(context) {
            const response = await axios.get('/users/fetch/');
            context.commit('setUsers', users);
        },

        async addUser(context, user) {
            const response = await axios.post('/users/add/', user );
            context.commit('addUser', newUser);
        },

        async deleteUser(context, user) {
            await axios.delete(`/users/delete/${user.id}`);
            context.commit('deleteUser', user);
        },

        async incrementUserScore(context, user) {
            const response = await axios.patch(`/users/increment/${user.id}`);
            context.commit('incrementUserScore', user);
        },

        async decrementUserScore(context, user) {
            const response = await axios.patch(`/users/decrement/${user.id}`);
            context.commit('decrementUserScore', user);
        }
    },
    }