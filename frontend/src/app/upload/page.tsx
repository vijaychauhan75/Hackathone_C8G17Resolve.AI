import DashboardShell from "@/features/dashboard/DashboardShell";

export default function UploadPage() {
  return (
    <DashboardShell>
      <div className="mx-auto max-w-3xl px-6 py-10">
        <h1 className="text-2xl font-semibold mb-2">Upload Logs</h1>
        <p className="text-slate-600 mb-6">
          Upload .txt or .log files to detect incidents.
        </p>

        <form className="rounded-lg border border-dashed p-10 text-center">
          <input
            type="file"
            accept=".txt,.log"
            className="mx-auto block"
            required
          />
          <p className="mt-2 text-sm text-slate-500">
            Accepted formats: .txt, .log
          </p>
        </form>
      </div>
    </DashboardShell>
  );
}