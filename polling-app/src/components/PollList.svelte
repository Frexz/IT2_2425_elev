<script>
    import PollDetails from "./PollDetails.svelte";
    import PollStore from '../stores/PollStore.js'
</script>

<div class="poll-list">
    {#each $PollStore as poll (poll.id)}
        <PollDetails {poll} />
    {/each}
</div>

<style>
    .poll-list {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
    }
</style>