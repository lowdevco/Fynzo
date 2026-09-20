/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./Fynzo/templates/**/*.html",
    "./Fynzo/apps/**/*.html",
  ],
  theme: {
    extend: {
      colors: {
        fynzo: {
          bg: '#0D1117',
          highlight: '#238636',
          panel: '#161b22',
          text: '#c9d1d9',
        }
      },
      fontFamily: {
        sans: ['Poppins', 'sans-serif'],
      }
    },
  },
  plugins: [],
}

