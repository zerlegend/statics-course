<script setup>
import { computed, reactive } from 'vue'
import { quizzes } from './quizzes.js'

const props = defineProps({ chapter: { type: String, required: true } })
const questions = computed(() => quizzes[props.chapter] || [])
const picked = reactive({})

const answered = computed(() => Object.keys(picked).length)
const correct = computed(() => questions.value.filter((q, i) => picked[i] === q.answer).length)

function choose(i, j) {
  if (picked[i] === undefined) picked[i] = j
}
function reset() {
  Object.keys(picked).forEach((k) => delete picked[k])
}
</script>

<template>
  <div class="quiz">
    <p class="quiz-title">Quick Quiz</p>
    <div v-for="(q, i) in questions" :key="i" class="quiz-q">
      <p class="quiz-text"><strong>{{ i + 1 }}.</strong> {{ q.q }}</p>
      <div class="quiz-options">
        <button
          v-for="(opt, j) in q.options"
          :key="j"
          type="button"
          class="quiz-opt"
          :class="{
            right: picked[i] !== undefined && j === q.answer,
            wrong: picked[i] === j && j !== q.answer,
            locked: picked[i] !== undefined
          }"
          @click="choose(i, j)"
        >{{ opt }}</button>
      </div>
      <p v-if="picked[i] !== undefined" class="quiz-why">
        <span v-if="picked[i] === q.answer">Correct.</span><span v-else>Not quite.</span> {{ q.why }}
      </p>
    </div>
    <p class="quiz-score">
      Score: {{ correct }} / {{ questions.length }}
      <span v-if="answered < questions.length"> ({{ answered }} answered)</span>
      <button type="button" class="quiz-reset" @click="reset">Reset</button>
    </p>
  </div>
</template>

<style scoped>
.quiz { border: 1px solid var(--vp-c-divider); border-radius: 10px; padding: 16px 18px; margin: 18px 0; background: var(--vp-c-bg-soft); }
.quiz-title { font-weight: 700; margin: 0 0 8px; font-size: 1.05rem; }
.quiz-q { margin: 14px 0; }
.quiz-text { margin: 0 0 6px; }
.quiz-options { display: flex; flex-wrap: wrap; gap: 8px; }
.quiz-opt { padding: 6px 12px; border: 1px solid var(--vp-c-divider); border-radius: 8px; background: var(--vp-c-bg); color: var(--vp-c-text-1); cursor: pointer; font-size: 0.92rem; }
.quiz-opt:hover:not(.locked) { border-color: var(--vp-c-brand-1); }
.quiz-opt.locked { cursor: default; }
.quiz-opt.right { border-color: #16a34a; background: rgba(22, 163, 74, 0.15); }
.quiz-opt.wrong { border-color: #dc2626; background: rgba(220, 38, 38, 0.15); }
.quiz-why { margin: 6px 0 0; font-size: 0.9rem; color: var(--vp-c-text-2); }
.quiz-score { margin: 10px 0 0; font-weight: 600; }
.quiz-reset { margin-left: 12px; padding: 2px 10px; border: 1px solid var(--vp-c-divider); border-radius: 6px; background: var(--vp-c-bg); color: var(--vp-c-text-1); cursor: pointer; font-size: 0.85rem; }
</style>
