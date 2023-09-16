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
              <th @click="toggleNameSort">Name</th>
              <th></th>
              <th></th>
              <th @click="togglePointSort">Score</th>
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
        sortOrder: '',
        sortHeader: '',
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
    
    async mounted() {
        await this.fetchUsers();
        this.displayedUsers = this.users;
        this.filterAndSortUsers('points', 'desc');
    },

    watch: {
      searchFilter(value) {
        if(value){
          this.displayedUsers = this.filteredUsers;
        } else {
          this.displayedUsers = this.users;
        }
      },

      users() {
        console.log("users changed");
        this.filterAndSortUsers(this.sortHeader, this.sortOrder);
    },
    },

    methods: {
        async fetchUsers() {
            await this.$store.dispatch('userLeaderboards/fetchUsers');
        },
        handleDelete(id) {
            this.$store.dispatch('userLeaderboards/deleteUser', id);
        },
        async handleIncrement(user) {
            await this.$store.dispatch('userLeaderboards/incrementUserScore', user);
            this.filterAndSortUsers(this.sortHeader, this.sortOrder);
        },
        async handleDecrement(user) {
            await this.$store.dispatch('userLeaderboards/decrementUserScore', user);
            this.filterAndSortUsers(this.sortHeader, this.sortOrder);
        },

      showUserDetailsDialog(user) {
        this.selectedUser = user;
        this.showUserDetails = true;
      },

      toggleNameSort() {
        console.log("function called");
        if (this.sortHeader === 'name') {
          if (this.sortOrder === 'asc') {
            this.filterAndSortUsers('name', 'desc');
          } else {
            this.filterAndSortUsers('name', 'asc');
          }
        } else {
          this.filterAndSortUsers('name', 'asc');
        }
      },

      togglePointSort() {
        
        if (this.sortHeader === 'points') {
          if (this.sortOrder === 'asc') {
            this.filterAndSortUsers('points', 'desc');
          } else {
            this.filterAndSortUsers('points', 'asc');
          }
        } else {
          this.filterAndSortUsers('points', 'asc');
        }
      },

      filterAndSortUsers(newSortHeader, newSortOrder){
        let results = this.users;
        this.sortHeader = newSortHeader;
        this.sortOrder = newSortOrder;
        if (this.searchFilter) {
          results.filter(user => {
            return user.name.toLowerCase().includes(this.searchFilter.toLowerCase());
          });
        }

        this.displayedUsers = results.sort((a, b) => {
          if (this.sortHeader === 'points'){
          if (this.sortOrder === 'asc') {
            return a[this.sortHeader] - b[this.sortHeader];
          } else {
            return b[this.sortHeader] - a[this.sortHeader];
          }
        } else if (this.sortHeader === 'name') {
          if (this.sortOrder === 'asc') {
            return a[this.sortHeader].localeCompare(b[this.sortHeader]);
          } else {
            return b[this.sortHeader].localeCompare(a[this.sortHeader]);
          }
        }
        });

      }
      //
    }

  };
  </script>
  