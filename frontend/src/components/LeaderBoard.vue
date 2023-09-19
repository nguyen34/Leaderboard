<template>
    <v-container fluid>
      <div>
        <h1>LeaderBoard</h1>
        <v-text-field class="mt-4" v-model="searchFilter" label="Search by Name" variant="outlined"></v-text-field>
        <div class="fix-table-head">
        <table>
          <thead>
            <tr>
              <th></th>
              <th @click="toggleNameSort" class="clickable align-center px-4">Name  <v-icon :class="{ 'invisible': sortHeader !== 'name' }" :icon="sortOrder ==='asc' ? 'mdi-chevron-down' : 'mdi-chevron-up'"/></th>
              <th></th>
              <th></th>
              <th @click="togglePointSort" class="clickable align-center px-4">Score <v-icon :class="{ 'invisible': sortHeader !== 'points' }" :icon="sortOrder ==='asc' ? 'mdi-chevron-down' : 'mdi-chevron-up'"/> </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in displayedUsers" :key="user.id" class="my-4">
             <td><v-btn variant="outlined" @click="handleDelete(user)"><v-icon icon="mdi-close"/></v-btn></td>
              <td class="px-4"><span @click="showUserDetailsDialog(user)" class="clickable truncate">{{ user?.name }}</span></td>
              <td class="pl-4"><v-btn variant="outlined" @click="handleIncrement(user)"><v-icon icon="mdi-plus"/></v-btn></td>
              <td class="pr-4"><v-btn :disabled="user.points === 0" variant="outlined" @click="handleDecrement(user)"><v-icon icon="mdi-minus"/></v-btn></td>
              <td class="px-4">{{ user.points }}</td>
            </tr>
          </tbody>
        </table>
      </div>
        <AddNewUserModal @user-added="filterAndSortUsers(sortHeader, sortOrder)" />
        <v-dialog v-model="showUserDetails">
          <v-card class="w-50 ma-auto">
            <v-card-title>
              <span class="headline">User Details</span>
            </v-card-title>
            <v-card-text>
              <div>Name: {{ selectedUser?.name }}</div>
              <div>Age: {{ selectedUser?.age }}</div>
              <div>Address: {{ selectedUser?.address }}</div>
              <div>Points: {{ selectedUser?.points }}</div>
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

  import { mapState, mapActions } from 'vuex';
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
    },
    
    async mounted() {
        await this.getUsers();
        this.displayedUsers = this.users;
        this.filterAndSortUsers('points', 'desc');
    },

    watch: {
      searchFilter() {
        this.filterAndSortUsers(this.sortHeader, this.sortOrder);
      },

      users() {
        this.filterAndSortUsers(this.sortHeader, this.sortOrder);
    },
    },

    methods: {
      ...mapActions('userLeaderboards', ['fetchUsers', 'deleteUser', 'incrementUserScore', 'decrementUserScore']),
        async getUsers() {
            await this.fetchUsers();
        },
        async handleDelete(id) {
            await this.deleteUser(id);
        },
        async handleIncrement(user) {
            await this.incrementUserScore(user);
            this.filterAndSortUsers(this.sortHeader, this.sortOrder);
        },
        async handleDecrement(user) {
            await this.decrementUserScore(user); 
            this.filterAndSortUsers(this.sortHeader, this.sortOrder);
        },

      showUserDetailsDialog(user) {
        this.selectedUser = user;
        this.showUserDetails = true;
      },

      toggleNameSort() {
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
          results = results.filter(user => {
            return user?.name.toLowerCase().includes(this.searchFilter.toLowerCase());
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
  
  <styles lang="scss" scoped>
  .clickable {
    cursor: pointer;
  }
  
  .invisible {
    visibility: hidden;
  }

  .truncate {
    width: 200px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .fix-table-head {
      overflow-y: auto;
      height: 75vh;
    }

  .fix-table-head thead th {
    position: sticky;
    top: 0;
    background: #4A4A4A;
    z-index: 10;
    border: 2px solid #616161;
    
  }

  table {
    border-collapse: collapse;        
    width: 100%;
  }

  th, td {
    padding: 8px 15px;
    border: 2px solid #616161;
  }

  th {
    background: #4A4A4A;
    opacity: 1;
  }
  
  </styles>