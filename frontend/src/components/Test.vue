<template>
    <div>
        <h1>Test</h1>
        <p>Test</p>
    </div>
</template>

<script>

export default {
    name: 'TestComponent',
    mounted() {
        console.log('Component mounted.')
        this.$axios.get('/users/test/').then(response => {
            console.log(response.data)
        }).catch(error => {
            console.log(error)
        })
    }
}   


</script>