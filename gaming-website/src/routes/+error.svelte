<script>
    export let data
    let error = data.error
    let status = data.status
</script>

<div class="error">
    <h2>Ooops! {status}</h2>
    <p>{error.message}</p>
    <a href="/">Take Me Home</a>
</div>

<style>
    .error {
        text-align: center;
        margin-bottom: 60px;
    }
</style>
