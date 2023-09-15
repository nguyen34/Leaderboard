<template>
    <v-container fluid>
      <!-- Add your work here -->
      <div>
        <h1>LeaderBoard</h1>
        <v-text-field v-model="searchFilter" label="Search by Name" variant="outlined"></v-text-field>
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
            <tr v-for="(user, index) in displayedUsers" :key="user.id">
             <td><v-btn variant="outlined" @click="handleDelete(user)">X</v-btn></td>
              <td>{{ index + 1 }}</td>
              <td><span @click="showUserDetailsDialog(user)">{{ user.name }}</span></td>
              <td><v-btn variant="outlined" @click="handleIncrement(user)">+</v-btn></td>
              <td><v-btn variant="outlined" @click="handleDecrement(user)">-</v-btn></td>
              <td>{{ user.points }}</td>
            </tr>
          </tbody>
        </table>
        <AddNewUserModal />
        <v-dialog v-model="showUserDetails">
          <v-card>
            <v-card-title>
              <span class="headline">User Details</span>
            </v-card-title>
            <v-card-text>
              <div>Name: {{ selectedUser.name }}</div>
              <div>Age: {{ selectedUser.age }}</div>
              <div>Address: {{ selectedUser.address }}</div>
              <div>Points: {{ selectedUser.points }}</div>
            </v-card-text>
            <v-card-actions>
              <v-btn color="primary" block @click="showUserDetails = false">Close Dialog</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
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
        showUserDetails: false,
        selectedUser: null,
        searchFilter: '',
        displayedUsers: [],
        reverseScoreSort: false,
      }
    },

    computed: {
      ...mapState('userLeaderboards', ['users']),
      filteredUsers() {
        return this.users.filter(user => {
          return user.name.toLowerCase().includes(this.searchFilter.toLowerCase());
        });
      },
      
    },
    
    mounted() {
        this.fetchUsers();
        this.displayedUsers = this.users;
    },

    watch: {
      searchFilter(value) {
        if(value){
          this.displayedUsers = this.filteredUsers;
        } else {
          this.displayedUsers = this.users;
        }
      },
    },

    methods: {
        fetchUsers() {
            this.$store.dispatch('userLeaderboards/fetchUsers');
        },
        handleDelete(id) {
            this.$store.dispatch('userLeaderboards/deleteUser', id);
        },
        handleIncrement(user) {
            this.$store.dispatch('userLeaderboards/incrementUserScore', user);
        },
        handleDecrement(user) {
            this.$store.dispatch('userLeaderboards/decrementUserScore', user);
        },

      showUserDetailsDialog(user) {
        this.selectedUser = user;
        this.showUserDetails = true;
      },
      //
    }

  };
  </script>
  