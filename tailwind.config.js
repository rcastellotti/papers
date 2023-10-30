/** @type {import('tailwindcss').Config} */
module.exports = {
    darkMode: "class",
  
    content: ["./templates/**/*.jinja2", "./papers/*.md"],
    theme: {
      extend: {},
    },
    plugins: [],
  };