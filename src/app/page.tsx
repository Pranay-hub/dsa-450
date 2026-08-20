"use client";

import { useState, useMemo } from "react";
import Link from "next/link";
import problems from "@/data/problems.json";

const topicIcons: Record<string, string> = {
  "Array": "📊", "Matrix": "🔲", "String": "🔤", "Searching & Sorting": "🔍",
  "LinkedList": "🔗", "Binary Trees": "🌳", "Binary Search Trees": "🌲",
  "Greedy": "💰", "Graph": "🕸️", "Dynamic Programming": "📈",
  "Heap": "🏔️", "Stacks & Queues": "📚", "BackTracking": "🔄",
  "Trie": "🔤", "Bit Manipulation": "⚡",
  "Selection Sort": "Sort", "Insertion Sort": "Sort", "Bubble Sort": "Sort",
};

const topicColors: Record<string, string> = {
  "Array": "from-blue-500/20 to-blue-600/10 border-blue-500/30",
  "Matrix": "from-purple-500/20 to-purple-600/10 border-purple-500/30",
  "String": "from-green-500/20 to-green-600/10 border-green-500/30",
  "Searching & Sorting": "from-yellow-500/20 to-yellow-600/10 border-yellow-500/30",
  "LinkedList": "from-pink-500/20 to-pink-600/10 border-pink-500/30",
  "Binary Trees": "from-emerald-500/20 to-emerald-600/10 border-emerald-500/30",
  "Binary Search Trees": "from-teal-500/20 to-teal-600/10 border-teal-500/30",
  "Greedy": "from-orange-500/20 to-orange-600/10 border-orange-500/30",
  "Graph": "from-cyan-500/20 to-cyan-600/10 border-cyan-500/30",
  "Dynamic Programming": "from-red-500/20 to-red-600/10 border-red-500/30",
  "Heap": "from-amber-500/20 to-amber-600/10 border-amber-500/30",
  "Stacks & Queues": "from-indigo-500/20 to-indigo-600/10 border-indigo-500/30",
  "BackTracking": "from-rose-500/20 to-rose-600/10 border-rose-500/30",
  "Trie": "from-violet-500/20 to-violet-600/10 border-violet-500/30",
  "Bit Manipulation": "from-lime-500/20 to-lime-600/10 border-lime-500/30",
};

function getTopicSlug(topic: string): string {
  const topicMap: Record<string, string> = {
    "Binary Trees": "binary-trees",
    "Binary Search Trees": "binary-search-trees",
    "Searching & Sorting": "searching-sorting",
    "Stacks & Queues": "stacks-queues",
    "Dynamic Programming": "dynamic-programming",
    "Bit Manipulation": "bit-manipulation",
  };
  return topicMap[topic] || topic.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/-+$/, "");
}

type Problem = (typeof problems)[number];

export default function HomePage() {
  const [search, setSearch] = useState("");
  const [selectedTopic, setSelectedTopic] = useState<string | null>(null);
  const [selectedDifficulty, setSelectedDifficulty] = useState<string | null>(null);

  const topics = useMemo(() => {
    const map = new Map<string, number>();
    for (const p of problems) {
      const t = p.topic;
      map.set(t, (map.get(t) || 0) + 1);
    }
    return Array.from(map.entries()).sort((a, b) => b[1] - a[1]);
  }, []);

  const filteredProblems = useMemo(() => {
    let list = problems as Problem[];
    if (search) {
      const q = search.toLowerCase();
      list = list.filter(p => p.problem.toLowerCase().includes(q) || p.topic.toLowerCase().includes(q) || p.algorithm?.toLowerCase().includes(q));
    }
    if (selectedTopic) {
      list = list.filter(p => p.topic === selectedTopic);
    }
    if (selectedDifficulty) {
      list = list.filter(p => p.difficulty === selectedDifficulty);
    }
    return list;
  }, [search, selectedTopic, selectedDifficulty]);

  const stats = useMemo(() => {
    const solved = problems.filter(p => p.status === "solved").length;
    const easy = problems.filter(p => p.difficulty === "Easy").length;
    const medium = problems.filter(p => p.difficulty === "Medium").length;
    const hard = problems.filter(p => p.difficulty === "Hard").length;
    return { total: problems.length, solved, easy, medium, hard };
  }, []);

  const difficultyColor = (d: string) => {
    if (d === "Easy") return "text-easy";
    if (d === "Medium") return "text-medium";
    return "text-hard";
  };

  return (
    <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8">
      {/* Hero */}
      <div className="mb-10 text-center">
        <h1 className="text-4xl font-bold mb-3">
          <span className="text-primary">DSA</span> 450 Problem Sheet
        </h1>
        <p className="text-zinc-400 text-lg">Complete solutions with optimized code, explanations, and visualizations</p>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-2 sm:grid-cols-5 gap-3 mb-8">
        {[
          { label: "Total", value: stats.total, color: "text-foreground" },
          { label: "Solved", value: stats.solved, color: "text-primary" },
          { label: "Easy", value: stats.easy, color: "text-easy" },
          { label: "Medium", value: stats.medium, color: "text-medium" },
          { label: "Hard", value: stats.hard, color: "text-hard" },
        ].map(s => (
          <div key={s.label} className="rounded-lg bg-surface border border-border p-3 text-center">
            <div className={`text-2xl font-bold ${s.color}`}>{s.value}</div>
            <div className="text-xs text-zinc-500">{s.label}</div>
          </div>
        ))}
      </div>

      {/* Search */}
      <div className="mb-6">
        <input
          type="text"
          placeholder="Search problems, topics, or algorithms..."
          value={search}
          onChange={e => setSearch(e.target.value)}
          className="w-full rounded-lg border border-border bg-surface px-4 py-3 text-foreground placeholder-zinc-500 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary transition-all"
        />
      </div>

      {/* Topic Cards */}
      {!selectedTopic && !search && (
        <div className="mb-10">
          <h2 className="text-lg font-semibold mb-4">Topics</h2>
          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3">
            {topics.map(([topic, count]) => (
              <button
                key={topic}
                onClick={() => setSelectedTopic(topic)}
                className={`rounded-xl border bg-gradient-to-br p-4 text-left transition-all hover:scale-[1.02] hover:shadow-lg ${topicColors[topic] || "from-zinc-500/20 to-zinc-600/10 border-zinc-500/30"}`}
              >
                <div className="text-sm font-medium mb-1">{topic}</div>
                <div className="text-xs text-zinc-400">{count} problems</div>
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Filters */}
      <div className="flex items-center gap-3 mb-4 flex-wrap">
        {selectedTopic && (
          <div className="flex items-center gap-2 rounded-full bg-primary/10 border border-primary/30 px-3 py-1 text-sm">
            <span>{selectedTopic}</span>
            <button onClick={() => setSelectedTopic(null)} className="text-primary hover:text-primary-hover">✕</button>
          </div>
        )}
        {selectedDifficulty && (
          <div className={`flex items-center gap-2 rounded-full border px-3 py-1 text-sm ${
            selectedDifficulty === "Easy" ? "bg-easy/10 border-easy/30" :
            selectedDifficulty === "Medium" ? "bg-medium/10 border-medium/30" :
            "bg-hard/10 border-hard/30"
          }`}>
            <span>{selectedDifficulty}</span>
            <button onClick={() => setSelectedDifficulty(null)} className="currentColor opacity-60 hover:opacity-100">✕</button>
          </div>
        )}
        <div className="flex gap-1 ml-auto">
          {["Easy", "Medium", "Hard"].map(d => (
            <button
              key={d}
              onClick={() => setSelectedDifficulty(selectedDifficulty === d ? null : d)}
              className={`rounded-full px-3 py-1 text-xs font-medium transition-all ${
                selectedDifficulty === d
                  ? d === "Easy" ? "bg-easy text-black" : d === "Medium" ? "bg-medium text-black" : "bg-hard text-white"
                  : "bg-surface border border-border text-zinc-400 hover:text-foreground"
              }`}
            >
              {d}
            </button>
          ))}
        </div>
      </div>

      {/* Problem List */}
      <div className="space-y-1">
        {filteredProblems.map((p, i) => (
          <Link
            key={p.id}
            href={`/problem/${p.id}`}
            className="flex items-center gap-4 rounded-lg border border-transparent px-4 py-3 hover:bg-surface hover:border-border transition-all group"
          >
            <span className="text-zinc-600 text-sm w-8 text-right shrink-0">{i + 1}</span>
            <div className="flex-1 min-w-0">
              <div className="text-sm font-medium truncate group-hover:text-primary transition-colors">{p.problem}</div>
              <div className="text-xs text-zinc-500 mt-0.5">{p.topic} {p.algorithm ? `· ${p.algorithm}` : ""}</div>
            </div>
            <span className="text-xs text-zinc-600 hidden sm:block">{p.timeComplexity}</span>
            <span className={`text-xs font-medium ${difficultyColor(p.difficulty)}`}>{p.difficulty}</span>
            {p.status === "solved" && <span className="text-success text-sm">✓</span>}
          </Link>
        ))}
        {filteredProblems.length === 0 && (
          <div className="text-center py-16 text-zinc-500">No problems found</div>
        )}
      </div>
    </div>
  );
}
