import { ProblemView } from "@/components/ProblemView";
import problems from "@/data/problems.json";

export function generateStaticParams() {
  return (problems as typeof problems).map(p => ({ id: p.id }));
}

export default async function ProblemPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  return <ProblemView id={id} />;
}