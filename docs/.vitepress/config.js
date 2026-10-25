import { defineConfig } from 'vitepress'

// Set to false to hide the worked-solution pages until you want to release them
// (for example, after the tutorial session or assignment deadline).
const solutionsPublished = true

// Math: VitePress's built-in `markdown.math` option uses markdown-it-mathjax3
// (installed as a devDependency), so $...$ and $$...$$ work out of the box.
export default defineConfig({
  title: 'Engineering Mechanics I (CEng2021)',
  description: 'Course website for Engineering Mechanics I (Statics), Department of Civil Engineering',
  lang: 'en-US',
  base: '/statics-course/',
  cleanUrls: true,
  srcExclude: solutionsPublished ? [] : ['solutions/**'],
  ignoreDeadLinks: solutionsPublished ? false : [/\/solutions\//],

  lastUpdated: true,

  markdown: {
    math: true
  },

  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Syllabus', link: '/syllabus/course-info' },
      { text: 'Chapters', link: '/chapters/ch1-vectors' },
      { text: 'Resources', link: '/resources/textbooks' }
    ],

    sidebar: [
      {
        text: 'Syllabus',
        items: [
          { text: 'Start Here', link: '/start-here' },
          { text: 'Course Information', link: '/syllabus/course-info' },
          { text: 'Learning Outcomes', link: '/syllabus/learning-outcomes' },
          { text: 'Weekly Schedule', link: '/syllabus/schedule' },
          { text: 'Instructors', link: '/syllabus/instructors' },
          { text: 'Assessment & Grading', link: '/syllabus/assessment' },
          { text: 'Policies', link: '/syllabus/policies' },
          { text: 'FAQ', link: '/syllabus/faq' }
        ]
      },
      {
        text: 'Chapters',
        items: [
          { text: '1. Scalars & Vectors', link: '/chapters/ch1-vectors' },
          { text: '2. Force Systems', link: '/chapters/ch2-force-systems' },
          { text: '3. Equilibrium', link: '/chapters/ch3-equilibrium' },
          { text: '4. Simple Structures', link: '/chapters/ch4-structures' },
          { text: '5. Centroids', link: '/chapters/ch5-centroids' },
          { text: '6. Area Moments of Inertia', link: '/chapters/ch6-moments-inertia' },
          { text: '7. Friction', link: '/chapters/ch7-friction' }
        ]
      },
      ...(solutionsPublished ? [{
        text: 'Worked Solutions',
        collapsed: true,
        items: [
          { text: 'Chapter 1', link: '/solutions/ch1-solutions' },
          { text: 'Chapter 2', link: '/solutions/ch2-solutions' },
          { text: 'Chapter 3', link: '/solutions/ch3-solutions' },
          { text: 'Chapter 4', link: '/solutions/ch4-solutions' },
          { text: 'Chapter 5', link: '/solutions/ch5-solutions' },
          { text: 'Chapter 6', link: '/solutions/ch6-solutions' },
          { text: 'Chapter 7', link: '/solutions/ch7-solutions' }
        ]
      }] : []),
      {
        text: 'Resources',
        items: [
          { text: 'Textbooks', link: '/resources/textbooks' },
          { text: 'Reading Guide', link: '/resources/reading-guide' },
          { text: 'Formula Sheet', link: '/resources/formula-sheet' },
          { text: 'Feedback', link: '/resources/feedback' },
          { text: 'Changelog', link: '/resources/changelog' },
          { text: 'Licence & Credits', link: '/resources/licence' }
        ]
      }
    ],

    search: {
      provider: 'local'
    },


    footer: {
      message: 'Department of Civil Engineering, College of Engineering. Original material under CC BY-NC-SA 4.0.',
      copyright: 'CEng2021 · Academic Year 2026/2027'
    }
  }
})
