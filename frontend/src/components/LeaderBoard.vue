<template>
    <v-container fluid>
      <!-- Add your work here -->
      <div>
        <h1>LeaderBoard</h1>
        <table>
          <thead>
            <tr>
              <th></th>
              <th>Rank</th>
              <th>Name</th>
              <th></th>
              <th></th>
              <th>Score</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(user, index) in users" :key="user.id">
             <td><v-btn variant="outlined" @click="handleDelete(user)">X</v-btn></td>
              <td>{{ index + 1 }}</td>
              <td>{{ user.name }}</td>
              <td><v-btn variant="outlined" @click="handleIncrement(user)">+</v-btn></td>
              <td><v-btn variant="outlined" @click="handleDecrement(user)">-</v-btn></td>
              <td>{{ user.points }}</td>
            </tr>
          </tbody>
        </table>
        <v-btn variant="outlined">
            + Add New User
        </v-btn>
        <AddNewUserModal :open="openDialog" />
      </div>
    </v-container>
  </template>
  
  <script>

  import { mapState } from 'vuex';
  import AddNewUserModal from './AddNewUserModal.vue';

  
  export default {
    name: 'LeaderBoard',
    components: {
        AddNewUserModal,

      //
    },

    data() {
      return {
        openDialog: false,
        //
      }
    },

    computed: {
      ...mapState('userLeaderboards', ['users']),
      
    },
    
    mounted() {
        this.fetchUsers();
    },

    watch: {
      //
    },

    methods: {
        fetchUsers() {
            this.$store.dispatch('userLeaderboards/fetchUsers');
        },
        handleDelete(id) {
            this.$store.dispatch('userLeaderboards/deleteUser', id);
        },
        toggleNewUserDialog() {
            this.openDialog = !this.openDialog;
        },
        handleIncrement(user) {
            this.$store.dispatch('userLeaderboards/incrementUserScore', user);
        },
        handleDecrement(user) {
            this.$store.dispatch('userLeaderboards/decrementUserScore', user);
        },
      //
    }

  };
  </script>
  