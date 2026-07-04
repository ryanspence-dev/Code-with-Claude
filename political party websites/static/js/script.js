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

    const refModal = document.getElementById("ref-modal");
    const refButtons = document.querySelectorAll(".ref-term");

    if (refModal && refButtons.length) {
        const modalTitle = document.getElementById("ref-modal-title");
        const modalBody = document.getElementById("ref-modal-body");
        const closeButton = refModal.querySelector(".ref-modal-close");
        let lastTrigger = null;

        const onRefModalKeydown = (event) => {
            if (event.key === "Escape") {
                closeRefModal();
                return;
            }
            if (event.key === "Tab") {
                const focusable = refModal.querySelectorAll(
                    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
                );
                if (!focusable.length) {
                    return;
                }
                const first = focusable[0];
                const last = focusable[focusable.length - 1];
                if (event.shiftKey && document.activeElement === first) {
                    event.preventDefault();
                    last.focus();
                } else if (!event.shiftKey && document.activeElement === last) {
                    event.preventDefault();
                    first.focus();
                }
            }
        };

        function openRefModal(trigger) {
            lastTrigger = trigger;
            modalTitle.textContent = trigger.dataset.refTitle;
            modalBody.textContent = trigger.querySelector(".ref-term-body").textContent;
            refModal.hidden = false;
            document.body.classList.add("ref-modal-open");
            closeButton.focus();
            document.addEventListener("keydown", onRefModalKeydown);
        }

        function closeRefModal() {
            refModal.hidden = true;
            document.body.classList.remove("ref-modal-open");
            document.removeEventListener("keydown", onRefModalKeydown);
            if (lastTrigger) {
                lastTrigger.focus();
            }
        }

        refButtons.forEach((button) => {
            button.addEventListener("click", () => openRefModal(button));
        });

        refModal.querySelectorAll("[data-ref-close]").forEach((el) => {
            el.addEventListener("click", closeRefModal);
        });
    }
});
