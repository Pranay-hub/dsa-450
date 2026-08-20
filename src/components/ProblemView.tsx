"use client";

import { useState } from "react";
import Link from "next/link";
import problems from "@/data/problems.json";

type Problem = (typeof problems)[number];

function CodeBlock({ code, language }: { code: string; language: string }) {
  const [copied, setCopied] = useState(false);
  const copy = () => {
    navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };
  return (
    <div className="relative group">
      <button onClick={copy} className="absolute top-2 right-2 rounded bg-zinc-700/50 px-2 py-1 text-xs text-zinc-400 opacity-0 group-hover:opacity-100 transition-opacity hover:bg-zinc-600/50">
        {copied ? "Copied!" : "Copy"}
      </button>
      <pre className="!p-4 !text-[13px]"><code className={`language-${language}`}>{code}</code></pre>
    </div>
  );
}

export function ProblemView({ id }: { id: string }) {
  const problem = (problems as Problem[]).find(p => p.id === id);

  if (!problem) {
    return (
      <div className="mx-auto max-w-4xl px-4 py-16 text-center">
        <h1 className="text-2xl font-bold mb-4">Problem Not Found</h1>
        <Link href="/" className="text-primary hover:text-primary-hover">← Back to all problems</Link>
      </div>
    );
  }

  const [activeTab, setActiveTab] = useState<"python" | "cpp" | "java">("python");
  const tabs = [
    { key: "python" as const, label: "Python" },
    { key: "cpp" as const, label: "C++" },
    { key: "java" as const, label: "Java" },
  ];

  const diffColor = problem.difficulty === "Easy" ? "text-easy bg-easy/10 border-easy/30" :
    problem.difficulty === "Medium" ? "text-medium bg-medium/10 border-medium/30" :
    "text-hard bg-hard/10 border-hard/30";

  const topicSlug = problem.topic.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/-+$/, "");

  return (
    <div className="mx-auto max-w-4xl px-4 sm:px-6 py-8">
      <Link href="/" className="text-sm text-zinc-500 hover:text-foreground transition-colors mb-4 inline-block">← All Problems</Link>

      {/* Header */}
      <div className="mb-6">
        <h1 className="text-2xl sm:text-3xl font-bold mb-3">{problem.problem}</h1>
        <div className="flex flex-wrap items-center gap-2">
          <Link href={`/topic/${topicSlug}`} className="rounded-full bg-primary/10 border border-primary/30 px-3 py-1 text-xs font-medium text-primary hover:bg-primary/20 transition-colors">{problem.topic}</Link>
          <span className={`rounded-full border px-3 py-1 text-xs font-medium ${diffColor}`}>{problem.difficulty}</span>
          {problem.algorithm && <span className="rounded-full bg-zinc-800 border border-border px-3 py-1 text-xs text-zinc-400">{problem.algorithm}</span>}
        </div>
      </div>

      {/* Question */}
      {problem.question && (
        <div className="rounded-xl border border-border bg-surface p-5 mb-6">
          <div className="flex items-center justify-between mb-3">
            <h3 className="text-sm font-semibold text-zinc-300">Problem Statement</h3>
            {problem.link && (
              <a href={problem.link} target="_blank" rel="noopener noreferrer" className="text-xs text-primary hover:text-primary-hover transition-colors">
                View original ↗
              </a>
            )}
          </div>
          <p className="text-sm text-zinc-400 leading-relaxed whitespace-pre-line">{problem.question}</p>
        </div>
      )}

      {/* Complexity */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-6">
        <div className="rounded-lg bg-surface border border-border p-4">
          <div className="text-xs text-zinc-500 mb-1">Time Complexity</div>
          <div className="font-mono text-sm font-medium text-foreground">{problem.timeComplexity}</div>
        </div>
        <div className="rounded-lg bg-surface border border-border p-4">
          <div className="text-xs text-zinc-500 mb-1">Space Complexity</div>
          <div className="font-mono text-sm font-medium text-foreground">{problem.spaceComplexity}</div>
        </div>
      </div>

      {/* Explanation */}
      <div className="rounded-xl border border-border bg-surface p-5 mb-6">
        <h3 className="text-sm font-semibold mb-3 text-zinc-300">Explanation</h3>
        <p className="text-sm text-zinc-400 leading-relaxed whitespace-pre-line">{problem.explanation}</p>
      </div>

      {/* Examples */}
      {problem.examples && problem.examples.length > 0 && (
        <div className="rounded-xl border border-border bg-surface p-5 mb-6">
          <h3 className="text-sm font-semibold mb-4 text-zinc-300">Examples</h3>
          <div className="space-y-4">
            {problem.examples.map((ex, i) => (
              <div key={i} className="rounded-lg bg-zinc-900 border border-border overflow-hidden">
                <div className="px-4 py-2 border-b border-border bg-zinc-800/50 text-xs font-medium text-zinc-400">Example {i + 1}</div>
                <div className="p-4 space-y-2 text-sm">
                  <div>
                    <span className="text-zinc-500 text-xs mr-2">Input:</span>
                    <code className="text-zinc-300 font-mono text-[13px]">{ex.input}</code>
                  </div>
                  <div>
                    <span className="text-zinc-500 text-xs mr-2">Output:</span>
                    <code className="text-success font-mono text-[13px]">{ex.output}</code>
                  </div>
                  {ex.explanation && (
                    <div>
                      <span className="text-zinc-500 text-xs mr-2">Explanation:</span>
                      <span className="text-zinc-400">{ex.explanation}</span>
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Notes */}
      {problem.notes && problem.notes !== "None" && (
        <div className="rounded-xl border border-warning/30 bg-warning/5 p-4 mb-6">
          <h3 className="text-xs font-semibold mb-2 text-warning">Your Notes</h3>
          <p className="text-sm text-zinc-400">{problem.notes}</p>
        </div>
      )}

      {/* Code Tabs */}
      <div className="rounded-xl border border-border bg-surface overflow-hidden mb-6">
        <div className="flex border-b border-border">
          {tabs.map(t => (
            <button
              key={t.key}
              onClick={() => setActiveTab(t.key)}
              className={`px-4 py-2.5 text-sm font-medium transition-colors ${
                activeTab === t.key
                  ? "text-primary border-b-2 border-primary bg-primary/5"
                  : "text-zinc-500 hover:text-foreground"
              }`}
            >
              {t.label}
            </button>
          ))}
        </div>
        {activeTab === "python" && <CodeBlock code={problem.solution.python} language="python" />}
        {activeTab === "cpp" && <CodeBlock code={problem.solution.cpp} language="cpp" />}
        {activeTab === "java" && <CodeBlock code={problem.solution.java} language="java" />}
      </div>

      {/* How the code works */}
      {problem.codeWalkthrough && problem.codeWalkthrough.length > 0 && (
        <div className="rounded-xl border border-border bg-surface p-5 mb-6">
          <h3 className="text-sm font-semibold mb-4 text-zinc-300">How the Code Works</h3>
          <ol className="space-y-3">
            {problem.codeWalkthrough.map((step, i) => (
              <li key={i} className="flex gap-3 text-sm text-zinc-400 leading-relaxed">
                <span className="shrink-0 w-6 h-6 rounded-full bg-primary/10 border border-primary/30 text-primary text-xs font-medium flex items-center justify-center mt-0.5">{i + 1}</span>
                <span>{step}</span>
              </li>
            ))}
          </ol>
        </div>
      )}

      {/* Navigation */}
      <div className="flex justify-between mt-8 pt-6 border-t border-border">
        {(() => {
          const idx = (problems as Problem[]).findIndex(p => p.id === id);
          const prev = idx > 0 ? (problems as Problem[])[idx - 1] : null;
          const next = idx < (problems as Problem[]).length - 1 ? (problems as Problem[])[idx + 1] : null;
          return (
            <>
              {prev ? (
                <Link href={`/problem/${prev.id}`} className="text-sm text-zinc-500 hover:text-primary transition-colors">← {prev.problem}</Link>
              ) : <span />}
              {next ? (
                <Link href={`/problem/${next.id}`} className="text-sm text-zinc-500 hover:text-primary transition-colors text-right">{next.problem} →</Link>
              ) : <span />}
            </>
          );
        })()}
      </div>
    </div>
  );
}
