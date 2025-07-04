/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        pink: {
          450: '#f472b6',
        },
        fuchsia: {
          550: '#c026d3',
        },
        purple: {
          650: '#7e22ce',
        },
      },
      dropShadow: {
        neon: '0 0 10px #ec4899',
        subtle: '0 0 4px #f472b6',
      },
      backdropBlur: {
        xs: '2px',
      },
      zIndex: {
        '-1': '-1',
        '-10': '-10',
      },
      animation: {
        'float-blob': 'floatBlob 22s ease-in-out infinite alternate',
      },
      keyframes: {
        floatBlob: {
          '0%': { transform: 'translate(0, 0) scale(1)' },
          '50%': { transform: 'translate(50px, -30px) scale(1.1)' },
          '100%': { transform: 'translate(-40px, 20px) scale(1)' },
        },
      },
    },
  },
  plugins: [],
}
