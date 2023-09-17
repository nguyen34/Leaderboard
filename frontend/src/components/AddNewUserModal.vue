<template>
    <div class="text-center">
      <v-btn
        variant="outlined"
        @click="dialog = true"
      >
        <v-icon left icon="mdi-plus"/>
         Add New User
      </v-btn>
  
      <v-dialog
        v-model="dialog"
        width="auto"
      >
        <v-card>
          <v-card-text>
            <!-- TODO: Add Form Validation. User can only enter numbers for age, and name and address cannot be blank-->
            <v-form v-model="isFormValid" @submit.prevent="handleSubmit">
              <v-text-field
                v-model="name"
                label="Name"
                :rules="textRules"
                required
              ></v-text-field>
              <v-text-field
                v-model="age"
                label="Age"
                type="number"
                :rules="numberRules"
                required
              ></v-text-field>
              <v-text-field
                v-model="address"
                label="Address"
                :rules="textRules"
                required
              ></v-text-field>
              <v-card-actions>
                <v-btn :disabled="!isFormValid" color="primary" block type="submit">Add User</v-btn>
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
  import { mapState, mapActions } from 'vuex';

  export default {
    name: "AddNewUserModal",
    data: () => ({
      dialog: false,
      name: '',
      age: 0,
      address: '',
      isFormValid: false,
      textRules: [
        v => !!v || 'Text is required',
      ],
      numberRules: [
        v => !!v || 'Number is required',
        v => (v > 0 && v <= 100) || 'Age must be between 1 and 100',
      ],
    }),

    computed: {
      ...mapState('userLeaderboards', ['users']),
    },
    methods: {
      ...mapActions('userLeaderboards', ['addUser']),
      close() {
        this.dialog = false;
      },
      async handleSubmit() {
        const user = {
          name: this.name,
          age: this.age,
          address: this.address,
        };
        await this.addUser(user);
        this.$emit('user-added');
        this.dialog = false;
      },
    },
  }
  </script>
  