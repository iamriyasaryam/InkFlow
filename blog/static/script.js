const form = document.querySelector(".Form");

if (form) {
    form.addEventListener("submit", function (event) {

        const title = document.querySelector("#title").value.trim();
        const author = document.querySelector("#author").value.trim();
        const content = document.querySelector("#content").value.trim();

        if (!title || !author || !content) {
            event.preventDefault();

            alert("Please fill in all fields.");
        }

    });
}

function confirmDelete() {
    return confirm("Are you sure you want to delete this post?");
}


const liveSearch = document.getElementById("live-search");
const liveResults = document.getElementById("live-results");

if (liveSearch) {
    liveSearch.addEventListener("input", function () {
        const query = liveSearch.value.trim();

        fetch(`/api/search/?q=${encodeURIComponent(query)}`)
            .then(response => response.json())
            .then(posts => {
                liveResults.innerHTML = "";

                if (posts.length === 0) {
                    liveResults.innerHTML = "<p>No posts found.</p>";
                    return;
                }

                posts.forEach(post => {
                    liveResults.innerHTML += `
                        <article class="post-card">
                            <h2>${post.title}</h2>
                            <p class="meta">
                                By ${post.author} · ${post.created_at}
                            </p>
                            <p>${post.content}...</p>
                            <a href="/post/${post.id}/">
                                Read More →
                            </a>
                        </article>
                    `;
                });
            })
            .catch(error => {
                console.error("Search error:", error);
            });
    });
}

console.log("InkFlow script loaded");