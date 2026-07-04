document.addEventListener("DOMContentLoaded", () => {
    const items = document.querySelectorAll(".accordion-item");

    items.forEach((item) => {
        const toggle = item.querySelector(".accordion-toggle");
        toggle.addEventListener("click", () => {
            item.classList.toggle("open");
        });
    });

    if (items.length) {
        items[0].classList.add("open");
    }

    const themeToggle = document.getElementById("theme-toggle");
    if (themeToggle) {
        const root = document.documentElement;

        const updateToggleState = () => {
            const isDark = root.classList.contains("dark-mode");
            themeToggle.setAttribute("aria-pressed", String(isDark));
            themeToggle.setAttribute("aria-label", isDark ? "Switch to light mode" : "Switch to dark mode");
        };

        updateToggleState();

        themeToggle.addEventListener("click", () => {
            root.classList.toggle("dark-mode");
            localStorage.setItem("theme", root.classList.contains("dark-mode") ? "dark" : "light");
            updateToggleState();
        });
    }

    const searchInput = document.getElementById("glossary-search");
    const glossaryItems = document.querySelectorAll(".glossary-item");
    const categoryButtons = document.querySelectorAll(".category-filter");
    const emptyMessage = document.getElementById("glossary-empty");

    if (searchInput && glossaryItems.length) {
        let activeCategory = "all";

        const applyFilters = () => {
            const query = searchInput.value.trim().toLowerCase();
            let visibleCount = 0;

            glossaryItems.forEach((item) => {
                const matchesCategory = activeCategory === "all" || item.dataset.category === activeCategory;
                const matchesSearch = !query || item.dataset.term.includes(query);
                const visible = matchesCategory && matchesSearch;
                item.hidden = !visible;
                if (visible) {
                    visibleCount++;
                }
            });

            if (emptyMessage) {
                emptyMessage.hidden = visibleCount !== 0;
            }
        };

        categoryButtons.forEach((button) => {
            button.addEventListener("click", () => {
                categoryButtons.forEach((btn) => {
                    btn.classList.remove("active");
                    btn.setAttribute("aria-pressed", "false");
                });
                button.classList.add("active");
                button.setAttribute("aria-pressed", "true");
                activeCategory = button.dataset.category;
                applyFilters();
            });
        });

        searchInput.addEventListener("input", applyFilters);
    }
});
