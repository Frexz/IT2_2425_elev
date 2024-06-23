<script>
    import PollDetails from "./PollDetails.svelte";
    import PollStore from '../stores/PollStore.js'

    export let polls = []

    PollStore.subscribe(data => {
        polls = data
    })
</script>

<div class="poll-list">
    {#each polls as poll (poll.id)}
        <PollDetails {poll} on:vote />
    {/each}
</div>

<style>
    .poll-list {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
    }
</style>