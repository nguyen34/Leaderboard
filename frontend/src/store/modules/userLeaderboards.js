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
            state.users[state.users.indexOf(user)].points--;
        }

    },

    actions: {
        async fetchUsers(context) {
            // const response = await this.$axios.get('/users');
            // const users = await response.data;
            const users = [
                // Hardcoded for now. We'll replace this with an API call later.
                {
                    id: 1,
                    name: 'Emma',
                    age : 25,
                    address: '1234 Main St',
                    points: 0,
                },
                {
                    id: 2,
                    name: 'Noah',
                    age : 30,
                    address: '1233 Min St',
                    points: 0,
                },
                {
                    id: 3,
                    name: 'James',
                    age : 35,
                    address: '1232 Main St',
                    points: 0,
                },
                {
                    id: 4,
                    name: 'William',
                    age : 40,
                    address: '1231 Main St',
                    points: 0,
                },
                {
                    id: 5,
                    name: 'Olivia',
                    age : 45,
                    address: '1230 Main St',
                    points: 0,
                },
            ];
            console.log("Users Fetched");
            context.commit('setUsers', users);
        },

        async addUser(context, user) {
            //const response = await this.$axios.post('/users/add', user);
            // const newUser = await response.data';
            console.log("Users Added");
            context.commit('addUser', user);
        },

        async deleteUser(context, user) {
            // await this.$axios.delete(`/users/delete/${user.id}`);
            console.log("Users Deleted");
            context.commit('deleteUser', user);
        },

        async incrementUserScore(context, user) {
            // await this.$axios.patch(`/users/increment/${user.id}`);
            console.log("Users Incremented");
            context.commit('incrementUserScore', user);
        },

        async decrementUserScore(context, user) {
            // await this.$axios.patch(`/users/decrement/${user.id}`);
            console.log("Users Decremented");
            context.commit('decrementUserScore', user);
        }
    },
    }