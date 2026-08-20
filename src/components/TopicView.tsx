"use client";

import { useState, useMemo } from "react";
import Link from "next/link";
import problems from "@/data/problems.json";

type Problem = (typeof problems)[number];

const topicNames: Record<string, string> = {
  "binary-trees": "Binary Trees",
  "binary-search-trees": "Binary Search Trees",
  "searching-sorting": "Searching & Sorting",
  "stacks-queues": "Stacks & Queues",
  "dynamic-programming": "Dynamic Programming",
  "bit-manipulation": "Bit Manipulation",
};

export function TopicView({ topic }: { topic: string }) {
  const topicName = topicNames[topic] || topic.split("-").map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(" ");

  const [search, setSearch] = useState("");
  const [diff, setDiff] = useState<string | null>(null);

  const topicProblems = useMemo(() => {
    let list = (problems as Problem[]).filter(p => p.topic === topicName);
    if (search) {
      const q = search.toLowerCase();
      list = list.filter(p => p.problem.toLowerCase().includes(q) || p.algorithm?.toLowerCase().includes(q));
    }
    if (diff) list = list.filter(p => p.difficulty === diff);
    return list;
  }, [topicName, search, diff]);

  const diffColor = (d: string) => d === "Easy" ? "text-easy" : d === "Medium" ? "text-medium" : "text-hard";

  return (
    <div className="mx-auto max-w-4xl px-4 sm:px-6 py-8">
      <Link href="/" className="text-sm text-zinc-500 hover:text-foreground transition-colors mb-4 inline-block">← All Problems</Link>
      <h1 className="text-2xl font-bold mb-2">{topicName}</h1>
      <p className="text-zinc-500 text-sm mb-6">{topicProblems.length} problems</p>

      <input
        type="text"
        placeholder={`Search ${topicName} problems...`}
        value={search}
        onChange={e => setSearch(e.target.value)}
        className="w-full rounded-lg border border-border bg-surface px-4 py-2.5 text-sm text-foreground placeholder-zinc-500 focus:outline-none focus:ring-2 focus:ring-primary/50 mb-4"
      />

      <div className="flex gap-1 mb-6">
        {["Easy", "Medium", "Hard"].map(d => (
          <button key={d} onClick={() => setDiff(diff === d ? null : d)}
            className={`rounded-full px-3 py-1 text-xs font-medium transition-all ${diff === d ? (d === "Easy" ? "bg-easy text-black" : d === "Medium" ? "bg-medium text-black" : "bg-hard text-white") : "bg-surface border border-border text-zinc-400 hover:text-foreground"}`}>
            {d}
          </button>
        ))}
      </div>

      <div className="space-y-1">
        {topicProblems.map((p, i) => (
          <Link key={p.id} href={`/problem/${p.id}`}
            className="flex items-center gap-4 rounded-lg border border-transparent px-4 py-3 hover:bg-surface hover:border-border transition-all group">
            <span className="text-zinc-600 text-sm w-8 text-right shrink-0">{i + 1}</span>
            <div className="flex-1 min-w-0">
              <div className="text-sm font-medium truncate group-hover:text-primary transition-colors">{p.problem}</div>
              <div className="text-xs text-zinc-500 mt-0.5">{p.algorithm}</div>
            </div>
            <span className="text-xs text-zinc-600 hidden sm:block">{p.timeComplexity}</span>
            <span className={`text-xs font-medium ${diffColor(p.difficulty)}`}>{p.difficulty}</span>
            {p.status === "solved" && <span className="text-success text-sm">✓</span>}
          </Link>
        ))}
        {topicProblems.length === 0 && <div className="text-center py-12 text-zinc-500">No problems found</div>}
      </div>
    </div>
  );
}
