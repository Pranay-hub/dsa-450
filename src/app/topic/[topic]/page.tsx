import { TopicView } from "@/components/TopicView";
import problems from "@/data/problems.json";

export function generateStaticParams() {
  const topics = [...new Set((problems as typeof problems).map(p => p.topic))];
  return topics.map(t => ({ topic: t.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/-+$/, "") }));
}

export default async function TopicPage({ params }: { params: Promise<{ topic: string }> }) {
  const { topic } = await params;
  return <TopicView topic={topic} />;
}