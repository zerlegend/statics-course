import DefaultTheme from 'vitepress/theme'
import Quiz from './Quiz.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('Quiz', Quiz)

    // Click a figure to zoom it; click again (or press Esc) to close.
    if (typeof window !== 'undefined') {
      document.addEventListener('click', (e) => {
        const t = e.target
        if (t && t.tagName === 'IMG' && t.closest('.vp-doc') && !t.closest('a')) {
          t.classList.toggle('zoomed')
          document.body.classList.toggle('has-zoom', t.classList.contains('zoomed'))
        } else {
          document.querySelectorAll('.vp-doc img.zoomed').forEach((i) => i.classList.remove('zoomed'))
          document.body.classList.remove('has-zoom')
        }
      })
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
          document.querySelectorAll('.vp-doc img.zoomed').forEach((i) => i.classList.remove('zoomed'))
          document.body.classList.remove('has-zoom')
        }
      })
    }
  }
}
