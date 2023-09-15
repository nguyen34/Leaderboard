<template>
    <div class="text-center">
      <v-btn
        variant="outlined"
        @click="dialog = true"
      >
        + Add New User
      </v-btn>
  
      <v-dialog
        v-model="dialog"
        width="auto"
      >
        <v-card>
          <v-card-text>
            <v-form @submit.prevent="handleSubmit">
              <v-text-field
                v-model="name"
                label="Name"
                required
              ></v-text-field>
              <v-text-field
                v-model="age"
                label="Age"
                required
              ></v-text-field>
              <v-text-field
                v-model="address"
                label="Address"
                required
              ></v-text-field>
              <v-card-actions>
                <v-btn color="primary" block type="submit">Add User</v-btn>
              </v-card-actions>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" block @click="close()">Close Dialog</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>
  </template>
  
  <script>
  import { mapState } from 'vuex';

  export default {
    name: "AddNewUserModal",
    data: () => ({
      dialog: false,
      name: '',
      age: 0,
      address: '',
    }),

    computed: {
      ...mapState('userLeaderboards', ['users']),
    },
    methods: {
      close() {
        this.dialog = false;
      },
      handleSubmit() {
        const user = {
          name: this.name,
          age: this.age,
          address: this.address,
        };
        this.$store.dispatch('userLeaderboards/addUser', user);
        this.dialog = false;
      },
    },
  }
  </script>
  