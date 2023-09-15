<template>
    <v-dialog v-model="open" max-width="500px">
        <v-card>
        <v-card-title>
            <span class="headline">Add New User</span>
        </v-card-title>
    
    
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
            <v-btn color="blue darken-1" text @click="save">Save</v-btn>
        </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
export default {
    name: "AddNewUserModal",
    props: {
        open: {
            type: Boolean,
            required: true,
        }
    },
}
</script>