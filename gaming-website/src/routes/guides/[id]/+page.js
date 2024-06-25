import { redirect } from '@sveltejs/kit'
export async function load({ fetch, params }) {
    const id = params.id
    const res = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`)
    const guide = await res.json()

    if (res.ok) {
        return {
            guide
        }
    }

    throw redirect(301, '/guides')
}